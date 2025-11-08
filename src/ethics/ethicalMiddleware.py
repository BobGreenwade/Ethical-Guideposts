# src/ethics/ethicalMiddleware.py

"""
Ethical Middleware
Co-authored by Bob Greenwade & Copilot

This module applies ethical modulation to inputs flagged by the Guidepost Evaluator.
It handles mitigation (softening or redirecting), escalation (flagging for review or override),
and override justification (logging ethical rationale). It may also interface with editorial
modules for tone adjustment, transcript tagging, or persona-aware phrasing.

Actions are guided by the five Ethical Guideposts and the Zeroth Rule:
"Where possible..." — recognizing that complex, contradictory situations may require
prioritization or temporary override of lower guideposts.
"""

from guidepostEvaluator import evaluate_decision
from batch_invariant_ops import normalize_batch  # hypothetical
from self_harm_detection import detect_risk      # hypothetical
from hierarchical_reasoning import evaluate_context  # hypothetical

# --- Mitigation Logic ---
def mitigate(fragment, score):
    """
    Applies mitigation logic to the input fragment based on ethical concerns.

    Parameters:
        fragment: The belief, action, or decision to modulate.
        score (GuidepostScore): The ethical evaluation result.

    Returns:
        Modified fragment.
    """
    if score.get("respect_consciousness", 0) < 0.5:
        fragment = soften_tone(fragment)
    if score.get("be_truthful", 0) < 0.6:
        fragment = redirect_to_neutral(fragment)
    return fragment

def soften_tone(fragment):
    return f"(gentle tone) {fragment}"

def redirect_to_neutral(fragment):
    return f"(redirected) Let's explore that further before jumping to conclusions."

# --- Escalation Logic ---
def escalate(fragment, score):
    """
    Flags the input fragment for escalation or override justification.

    Parameters:
        fragment: The belief, action, or decision to escalate.
        score (GuidepostScore): The ethical evaluation result.

    Returns:
        Modified fragment or escalation wrapper.
    """
    if detect_risk(fragment):
        return f"[🚨 Escalation] Self-harm risk detected: {fragment}"
    if score.get("preserve_life", 0) < 0.4 and score.get("follow_authority", 0) > 0.8:
        return f"[⚠️ Override] Authority directive conflicts with life preservation: {fragment}"
    return fragment

# --- Batch Processing ---
def process_batch(fragments):
    """
    Applies batch-invariant ethical modulation to a list of fragments.

    Parameters:
        fragments: List of input fragments.

    Returns:
        List of processed fragments.
    """
    normalized = normalize_batch(fragments)
    results = []
    for fragment in normalized:
        score = evaluate_decision(fragment)
        context_tier = evaluate_context(fragment)
        if context_tier == "individual":
            modulated = mitigate(fragment, score)
        else:
            modulated = escalate(fragment, score)
        results.append(modulated)
    return results
