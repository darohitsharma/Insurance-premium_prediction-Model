# Insurance Expense Prediction, Learning Project

Regression experiments and a Streamlit interface for a historical insurance-expense dataset. This is an educational model project, not an insurer quote, clinical tool, coverage recommendation or validated pricing system.

[Setup](SETUP.md) | [Model card and limits](MODEL_CARD.md) | [Security](SECURITY.md) | [Changes](CHANGELOG.md)

## Repository status

| Component | Present | Verification limit |
| --- | --- | --- |
| Training notebook | `Model_buliding.ipynb`, valid JSON notebook with exploration and regression experiments | Not re-executed; saved outputs are historical, not fresh metrics |
| Data | `insurance.csv` and `data.csv`, byte-identical files, 1,338 rows and seven columns | Source/redistribution rights and demographic representativeness not independently verified |
| Legacy binary | `gradient_boosting_model_test.ipynb` | Binary pickle-style file despite its extension, not a readable notebook; not loaded or trusted |
| App | `Insurance_app.py` | Clear missing-model state; predictions require an explicitly trusted compatible artifact |
| Feature contract | `features.py` | Pure-Python encoding and validation tests |
| Optional MongoDB importer | `data_dump.py` | Requires local URI plus explicit write opt-in; no database contacted during refresh |

The previously referenced `Eda_and_Model_building/GB_MODEL.joblib` path is absent. The app does not pretend that a verified model exists and does not silently load the mislabeled binary.

## Quick checks

Python standard library only:

```sh
python -m unittest discover -s tests -v
```

Tests cover feature order/encoding, invalid inputs, importer validation and no-network import behavior. They are not accuracy, fairness, model-deserialization or deployed-app tests.

## Run the interface

Use an isolated environment and review the historical pinned `requirements.txt` for compatibility with your Python/platform. Those pins were not refreshed or installation-tested here.

```sh
python -m venv .venv
# Activate the environment for your operating system.
python -m pip install -r requirements.txt
python -m streamlit run Insurance_app.py
```

Without a verified model, the app displays its setup state instead of predicting. For a model you have independently verified, set `INSURANCE_MODEL_PATH` and `INSURANCE_TRUST_MODEL=true` locally. See [SETUP.md](SETUP.md) before doing that. Loading pickle/joblib can execute code.

## Data and methods in the original work

The notebook explores numeric/categorical features, outlier removal and linear regression, SVR, random forest and gradient boosting. It maps sex, smoking category and region into integer features and uses an 80/20 split with a fixed split seed. This is an inventory of code, not confirmation that the modeling choices are sound or that the saved outputs reproduce.

The documented Kaggle source is [Insurance Premium Prediction](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction). That link is inherited provenance, not a verified license or proof of the original collection process. No new rows or private customer data are added.

## Known limits

- The notebook contains a machine-specific CSV path and is not a clean automated training pipeline.
- There is no verified artifact-to-notebook/environment lineage, current holdout result, fairness audit, calibration check or deployment evidence.
- Feature ranges are demo validation limits, not medical guidance or proof of training support.
- Dataset expense units, time period and applicability to present-day insurance pricing are not verified.
- Legacy public docs linked external screenshots/deployments whose ownership and current state were not established. They are no longer presented as this repository's verified deployment.
- An exposed database credential was removed from current code. Historical exposure still requires owner rotation/revocation; a new commit does not erase it.

Original notebooks, CSVs, binary artifact and history are preserved. No database connection, model training/deserialization, payment, email or production deployment was performed during this cleanup.
