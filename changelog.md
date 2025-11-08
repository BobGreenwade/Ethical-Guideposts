# Changelog

All notable changes to this project will be documented in this file.

---

## [0.2.0] - 2025-11-08
### Added
- Integrated Qwen3Guard for safety classification and override logic
- Added `batchInvariantOps.py` for consistent ethical scoring across batches
- Added `hierarchicalReasoning.py` to support context-tiered ethical evaluation
- Created `qwenGuardAdapter.py` to wrap Qwen3Guard logic
- Created `personalValues.py` for user-defined ethical modifiers
- Updated `integration.py` with essential module checks and humorous failure modes

### Updated
- `ethicalMiddleware.py` now uses Qwen3Guard and batch-invariant normalization
- `ethicalVector.py` now references Qwen3Guard and HRM for scoring
- `guidepostEvaluator.py` now supports safety-based overrides and personal value tuning

---

## [0.0.1] - 2025-10-30
### Added
- Initial scaffolding of core ethical modules:
  - `ethicalVector.py`: Generates ethical alignment vectors
  - `guidepostEvaluator.py`: Interprets vectors and applies override logic
  - `ethicalMiddleware.py`: Handles mitigation and escalation
- Defined the Five Ethical Guideposts and Zeroth Rule
- Established modular structure for future expansion
