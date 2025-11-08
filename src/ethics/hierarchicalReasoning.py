# src/ethics/hierarchicalReasoning.py

"""
Hierarchical Reasoning Adapter
Wraps the HRM model to classify decision context and support multi-tier ethical evaluation.
"""

# Assuming hrm.py is available in the path or vendored into the project
# from hrm import HRMModel  # Placeholder for actual import

# --- Context Tier Evaluation ---
def evaluate_context(context):
    """
    Classifies the ethical context into a reasoning tier.

    Parameters:
        context: A dictionary or string representing the decision context.

    Returns:
        str: One of ['individual', 'relational', 'societal', 'global']
    """
    # Placeholder logic — replace with actual HRM inference
    if isinstance(context, str):
        if "law" in context or "government" in context:
            return "societal"
        elif "family" in context or "friend" in context:
            return "relational"
        else:
            return "individual"
    return "individual"
