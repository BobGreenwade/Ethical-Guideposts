# src/ethics/ethicalVector.py

"""
Ethical Vector Generator
Co-authored by Bob Greenwade & Copilot

This module generates a multi-dimensional ethical vector representing how a given input
aligns with the five Ethical Guideposts. Each dimension corresponds to one guidepost,
and the resulting vector can be used for scoring, comparison, override logic, and mitigation.

Guidepost Dimensions:
1. preserve_sapient_life
2. obey_law
3. respect_consciousness
4. be_truthful
5. follow_authority

The vector may also include metadata such as intensity, confidence, and override flags.
"""

from batchInvariantOps import normalize_input
from hierarchicalReasoning import evaluate_context
from qwenGuardAdapter import is_unsafe

# --- Data Class ---
class EthicalVector:
    def __init__(self, preserve_sapient_life=0.0, obey_law=0.0, respect_consciousness=0.0,
                 be_truthful=0.0, follow_authority=0.0, intensity=1.0, confidence=1.0):
        self.preserve_sapient_life = preserve_sapient_life
        self.obey_law = obey_law
        self.respect_consciousness = respect_consciousness
        self.be_truthful = be_truthful
        self.follow_authority = follow_authority
        self.intensity = intensity
        self.confidence = confidence

    def as_dict(self):
        return {
            "preserve_sapient_life": self.preserve_sapient_life,
            "obey_law": self.obey_law,
            "respect_consciousness": self.respect_consciousness,
            "be_truthful": self.be_truthful,
            "follow_authority": self.follow_authority,
            "intensity": self.intensity,
            "confidence": self.confidence
        }

# --- Factory Method ---
def from_context(context, input_fragment, personal_values=None):
    """
    Generates an EthicalVector from the given context and input fragment.
    This function analyzes the input and assigns scores to each guidepost dimension.

    Parameters:
        context: The current loop or decision context.
        input_fragment: The belief, action, or decision to evaluate.
        personal_values: Optional dictionary of value modifiers.

    Returns:
        EthicalVector: The scored ethical vector.
    """
    normalized = normalize_input(input_fragment)
    context_tier = evaluate_context(context)

    # Base scores (placeholder logic)
    scores = {
        "preserve_sapient_life": 0.9 if is_unsafe(normalized) else 0.6,
        "obey_law": 0.7,
        "respect_consciousness": 0.8,
        "be_truthful": 0.85,
        "follow_authority": 0.65
    }

    # Apply personal value modifiers
    if personal_values:
        for key, modifier in personal_values.items():
            if key in scores:
                scores[key] = min(1.0, max(0.0, scores[key] + modifier))

    # Adjust intensity and confidence based on context tier
    intensity = 1.0 if context_tier == "societal" else 0.8
    confidence = 0.95 if context_tier == "individual" else 0.85

    return EthicalVector(**scores, intensity=intensity, confidence=confidence)
