# integration.py
# Initializes and validates core ethics dependencies for the Guideposts module.

import sys

ESSENTIAL = {
    "z3": "z3-solver",
    "durable_rules": "durable-rules",
    "self_harm_detection": "self-harm-detection",
    "batch_invariant_ops": "batch-invariant-ops",
    "hierarchical_reasoning": "hierarchical-reasoning-model"
}

def try_import(module_name, pip_name, critical=False):
    try:
        __import__(module_name)
        print(f"[✓] {module_name} loaded.")
    except ImportError:
        if critical:
            print(f"[💥] CRITICAL: {module_name} missing. Ethical collapse imminent. Install `{pip_name}`.")
            sys.exit(42)
        else:
            print(f"[⚠️] Optional module {module_name} not found. Skipping gracefully. Install `{pip_name}` for full functionality.")

def initialize_modules():
    print("🔧 Initializing Ethical Guideposts dependencies...\n")
    for mod, pip in ESSENTIAL.items():
        try_import(mod, pip, critical=True)
    print("\n✅ Initialization complete. Proceeding with ethical clarity.")

if __name__ == "__main__":
    initialize_modules()
