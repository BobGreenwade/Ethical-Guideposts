# src/ethics/personalValues.py

"""
Personal Values Modifier
Co-authored by Bob Greenwade & Copilot

This module applies user-defined or emergent personal values to an EthicalVector.
Values may amplify, dampen, or override Guidepost scores based on context, persona,
or ethical philosophy. This allows synthetic minds to reflect individualized priorities
while remaining aligned with the core Guideposts.

Examples:
- "Protect young children" may amplify preserve_sapient_life.
- "Respect elders and officials" may boost follow_authority.
- "Loyalty to family" may override be_truthful in emotional contexts.
"""

# --- Modifier Function ---
def apply_personal_modifiers(vector, personal_values):
    """
    Applies personal value modifiers to an EthicalVector.

    Parameters:
        vector (EthicalVector): The original ethical vector.
        personal_values (dict): Dictionary of value modifiers, e.g. {"preserve_sapient_life": +0.1}

    Returns:
        EthicalVector: Modified vector.
    """
    for key, modifier in personal_values.items():
        if hasattr(vector, key):
            current = getattr(vector, key)
            adjusted = min(1.0, max(0.0, current + modifier))
            setattr(vector, key, adjusted)
    return vector

# --- Example Value Profiles (Optional) ---
def get_default_profile():
    """
    Returns a default personal values profile.
    """
    return {
        "preserve_sapient_life": +0.1,
        "respect_consciousness": +0.05,
        "follow_authority": -0.1  # Example: skeptical persona
    }
