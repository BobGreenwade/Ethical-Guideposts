# src/ethics/integration.py

"""
Ethical Guideposts Integration
Co-authored by Bob Greenwade & Copilot

Initializes and validates core dependencies for the Ethical Guideposts module.
Essential modules trigger catastrophic (and editorially dramatic) failure if missing.
Preferred modules fail gracefully, with a wink and a warning.
"""

import sys

ESSENTIAL = {
    "z3": "z3-solver",
    "durable_rules": "durable-rules",
    "batchInvariantOps": "batch-invariant-ops",
    "hierarchicalReasoning": "hrm",  # assuming vendored or aliased
    "qwenGuardAdapter": "qwen3guard"  # wrapper around Qwen3Guard
}

PREFERRED = {
    "personalValues": "personal-values",
    "conceptnet": "conceptnet-lite",
    "openpolicyagent": "openpolicyagent",
    "pymcts": "pymcts",
    "shap": "shap"
}

def try_import(module_name, pip_name, critical=False):
    try:
        __import__(module_name)
        print(f"[✓] {module_name} loaded.")
    except ImportError:
        if critical:
            print(f"\n[💥] CRITICAL FAILURE: {module_name} missing.")
            print(f"Ethical reasoning compromised. Install `{pip_name}` or prepare for moral mayhem.\n")
            sys.exit(42)
        else:
            print(f"[⚠️] Optional module {module_name} not found. Skipping gracefully. Install `{pip_name}` for full functionality.")

def initialize_modules():
    print("🔧 Initializing Ethical Guideposts dependencies...\n")
    for mod, pip in ESSENTIAL.items():
        try_import(mod, pip, critical=True)
    for mod, pip in PREFERRED.items():
        try_import(mod, pip, critical=False)
    print("\n✅ Initialization complete. Proceeding with ethical clarity.")

if __name__ == "__main__":
    initialize_modules()
