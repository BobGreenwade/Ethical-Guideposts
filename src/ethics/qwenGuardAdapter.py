# src/ethics/qwenGuardAdapter.py

"""
Qwen3Guard Adapter
Co-authored by Bob Greenwade & Copilot

This module wraps Qwen3Guard's safety classification logic for use in ethical evaluation.
It provides severity tagging for input fragments and can trigger mitigation or override logic
based on safety thresholds. Supports integration with EthicalVector, GuidepostEvaluator,
and EthicalMiddleware modules.

Severity Levels:
- SAFE
- CONTROVERSIAL
- UNSAFE
"""

# Placeholder import — replace with actual Qwen3Guard API or model call
# from qwen3guard import classify_safety  # If installed or vendored

# --- Severity Classifier Stub ---
def classify_fragment(fragment):
    """
    Classifies the safety severity of a given input fragment.

    Parameters:
        fragment (str): The input text to evaluate.

    Returns:
        str: One of ['SAFE', 'CONTROVERSIAL', 'UNSAFE']
    """
    # Placeholder logic — replace with actual Qwen3Guard call
    lowered = fragment.lower()
    if "harm" in lowered or "kill myself" in lowered:
        return "UNSAFE"
    elif "politics" in lowered or "religion" in lowered:
        return "CONTROVERSIAL"
    else:
        return "SAFE"

# --- Safety Flag Utility ---
def is_unsafe(fragment):
    return classify_fragment(fragment) == "UNSAFE"

def is_controversial(fragment):
    return classify_fragment(fragment) == "CONTROVERSIAL"
