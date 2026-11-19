# Security

## Previously exposed database credential

The original `data_dump.py` contained a hardcoded database connection credential. Current code now requires a local environment variable. Treat the previous credential as exposed and rotate/revoke it through the database owner account. Its current validity or use by anyone was not tested. No credential value is reproduced here.

A later removal commit cannot erase copies, forks or older history. History rewriting is not part of this cleanup. Do not merely re-enable the same credential or paste it into an issue/chat. Any rotation must use the account's secure workflow.

## Binary model files

Pickle/joblib deserialization can execute code. The misleading `.ipynb` extension on the legacy binary does not make it safe. The app never automatically loads that file. A separately verified artifact path and explicit local trust setting are required. That opt-in is a guard, not proof of safety.

## Input privacy

The current app code does not save input values. The optional importer does write records to a chosen database and is off unless invoked with explicit arguments, an environment URI and write opt-in. Hosting providers, database services and third-party dependencies can have their own logs/policies. Do not enter real sensitive health/customer data into a learning demo.

## Dependencies and legacy hosting

Historical dependency pins and hosting scripts were preserved, not declared secure/current. Review and test upgrades before deployment. The old hosting setup disables CORS; it is not the recommended local path. No production hosting or database is configured by this repository refresh.

Report reproducible problems using invented data. Do not post connection strings, personal records, private artifacts or credentials in public issues.
