# Setup

## Checks that need no packages

```sh
python -m unittest discover -s tests -v
python -m py_compile Insurance_app.py features.py data_dump.py
```

These checks do not load the binary artifact, train a model or contact MongoDB. They do not install or test the historical Streamlit/scikit-learn pins.

## Model interface

The expected six features, in order, are:

| Feature | Encoding |
| --- | --- |
| age | Integer demo range 18 to 100 |
| sex | female=0, male=1, historical dataset categories only |
| bmi | Finite number greater than zero, demo maximum 100 |
| children | Integer 0 to 5 |
| smoker | no=0, yes=1 |
| region | southwest=1, southeast=2, northwest=3, northeast=4 |

Mappings are read from the existing notebook. They do not prove a given artifact was trained with that same contract. No new scaler is applied in the app; a model needing different preprocessing is incompatible unless it packages that preprocessing itself and accepts the documented input.

The file `gradient_boosting_model_test.ipynb` is binary, not notebook JSON. Do not open it with `pickle.load` or `joblib.load` just to inspect it. Such loading can run code. It is preserved as an unverified legacy artifact, not automatically adopted.

For a separately reviewed/trusted model, record its origin, hash, Python/scikit-learn/joblib versions, exact feature contract, training split and reproducible holdout results. Then set locally:

```sh
export INSURANCE_MODEL_PATH=/private/path/to/verified-model.joblib
export INSURANCE_TRUST_MODEL=true
python -m streamlit run Insurance_app.py
```

Use your operating system's environment-variable syntax. These are local operational choices, not an instruction to trust any file found in the repository. The missing default artifact path is `artifacts/model.joblib`. Model files under `artifacts/` are ignored by git.

## Notebook review

The notebook reads a machine-specific CSV path. Change that in a private working copy to the intended local dataset only after checking its provenance and schema. Do not call saved notebook outputs fresh evaluation. Design a reproducible training/export path before claiming the web app is model-validated.

The historical requirement pins remain unchanged for traceability. Use a compatible isolated Python environment, inspect installation errors and security advisories, and update/test dependencies deliberately. No claim is made that these pins install on every current Python release.

## Optional MongoDB importer

The app does not need MongoDB. The importer is a separate tool and should not be run for a demo.

`data_dump.py` requires a local `MONGODB_URI`, explicit database/collection arguments and `--allow-write`. Do not put credentials in command arguments, source, notebooks, logs or chat. Use an appropriate local secret mechanism. Do not reuse any credential historically exposed in this repository.

Install `pymongo` only if you intentionally need this optional workflow. Review file rights, target ownership and the effect before running. CSV values are ingested as strings, not model-ready feature values. Repeated runs can create duplicates; partial inserts may occur. Inspect state before retrying a failed write. No importer execution or database validation is included in this refresh.

## Historical hosting files

`Procfile` and `setup.sh` remain as legacy material. The shell setup disables CORS and writes hosting configuration. It is not used by the documented local path and has not been verified for a current hosting provider. Do not treat it as a production deployment recipe.
