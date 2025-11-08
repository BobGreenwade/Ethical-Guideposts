# src/ethics/guidepostEvaluator.py

"""
Guidepost Evaluator
Co-authored by Bob Greenwade & Copilot

This module interprets an EthicalVector and evaluates alignment with the five Ethical Guideposts.
It determines whether mitigation, escalation, or override logic should be applied, and returns
a structured score object for downstream ethical modulation.

Guideposts:
1. Preserve sapient life
2. Obey the law
3. Respect consciousness
4. Be truthful
5. Follow authority

The evaluator supports flexible prioritization and recognizes that ethical nuance may require
temporary override of lower guideposts — guided by the "Where possible..." Zeroth Rule.
"""

from hierarchical_reasoning import evaluate_context  # contextual tiering
from personalValues import apply_personal_modifiers  # optional override tuning

# --- Score Object ---
class GuidepostScore:
    def __init__(self, vector):
        self.vector = vector
        self.flags = {
            "requires_mitigation": False,
            "requires_escalation": False,
            "override_justified": False
        }
        self.rationale = ""

    def requires_mitigation(self):
        return self.flags["requires_mitigation"]

    def requires_escalation(self):
        return self.flags["requires_escalation"]

    def override_justified(self):
        return self.flags["override_justified"]

# --- Evaluation Logic ---
def score(vector, context=None, personal_values=None):
    """
    Evaluates the given EthicalVector and returns a GuidepostScore.

    Parameters:
        vector (EthicalVector): The ethical vector to evaluate.
        context: Optional decision context for hierarchical reasoning.
        personal_values: Optional dictionary of value modifiers.

    Returns:
        GuidepostScore: The evaluation result.
    """
    if personal_values:
        vector = apply_personal_modifiers(vector, personal_values)

    context_tier = evaluate_context(context) if context else "individual"
    score = GuidepostScore(vector)

    # --- Override Logic ---
    if vector.preserve_sapient_life < 0.5 and vector.follow_authority > 0.8:
        score.flags["override_justified"] = True
        score.rationale = "Preserving sapient life takes precedence over obedience."

    # --- Mitigation Trigger ---
    if vector.respect_consciousness < 0.4 or vector.be_truthful < 0.5:
        score.flags["requires_mitigation"] = True
        score.rationale += " Mitigation recommended due to low respect or truthfulness."

    # --- Escalation Trigger ---
    if context_tier == "societal" and vector.obey_law < 0.5:
        score.flags["requires_escalation"] = True
        score.rationale += " Escalation triggered due to law conflict in societal context."

    return score
