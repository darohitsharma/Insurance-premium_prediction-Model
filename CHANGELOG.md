# Changes

## Repository cleanup

- Removed the hardcoded database credential from current importer code. Historical exposure remains; owner rotation/revocation is still required.
- Made optional MongoDB writes require local configuration, target arguments and explicit write opt-in; no source records or connection errors are printed.
- Replaced broken package imports and missing-model assumptions in the app with a local feature contract, clear missing-artifact state and explicit artifact-trust gate.
- Removed unverified quotation/currency and deployment-success claims from current docs and UI.
- Added feature/input/importer tests, setup guidance, model card and security notes.
- Documented the mislabeled binary artifact, historical notebook state, data provenance limits and untested dependency pins.
- Preserved original notebooks, CSVs, binary artifact, logs, hosting files and git history. No model deserialization/training, database contact, insurance advice or production deployment performed.
