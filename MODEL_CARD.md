# Model card, repository evidence only

## Intended use

Learning about regression and a small inference UI. Not insurance underwriting, coverage selection, medical judgment, financial planning or a current insurer quotation. Do not make decisions affecting a person from this output.

## Data evidence

The repository contains two identical CSVs, each with 1,338 rows and columns age, sex, bmi, children, smoker, region and expenses. Existing documentation names a Kaggle dataset. The original data collection process, license, geography/currency/coverage period, consent and representativeness have not been independently verified here. Existing records are preserved; no new data is collected.

## Training evidence

`Model_buliding.ipynb` contains exploration, z-score outlier removal, integer categorical mappings and experiments with linear regression, SVR, random forest and gradient boosting. It uses a fixed-seed train/test split. This refresh did not execute the notebook or certify model selection. No performance number is promoted from saved outputs into a fresh-result claim.

## Artifact evidence

The app's old configured artifact path is absent. A separate file ending in `.ipynb` has binary pickle-style content. It was not deserialized, evaluated, renamed into a trusted model or used for predictions. Artifact origin, compatibility and linkage to training remain unresolved.

## Evaluation needed

- Reproducible preprocessing and train/validation/test separation, with leakage review.
- Documented target meaning, units and period.
- Baseline and holdout metrics with uncertainty, not only a selected model score.
- Subgroup error/fairness analysis, especially for sensitive demographic variables.
- Out-of-distribution/range checks and explicit missing-category policy.
- Artifact hash and environment lineage, inference-contract tests and dependency review.

No fairness, clinical validity, causal interpretation, calibration or present-day pricing reliability is claimed. The UI's finite/range checks are only software input checks.
