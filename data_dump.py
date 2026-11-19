"""Optional explicit CSV import. No network connection occurs on import.

Requires owner-supplied local MONGODB_URI and --allow-write at execution.
Never print the URI or source records. No credential is stored in this file.
"""
import argparse
import csv
import os
from pathlib import Path


def read_records(path):
    with Path(path).open(newline='', encoding='utf-8-sig') as source:
        reader = csv.DictReader(source)
        expected = {'age', 'sex', 'bmi', 'children', 'smoker', 'region', 'expenses'}
        if set(reader.fieldnames or []) != expected:
            raise ValueError('CSV header must match the documented seven-column contract.')
        return list(reader)


def main(argv=None):
    parser = argparse.ArgumentParser(description='Optional one-time CSV import into your own MongoDB.')
    parser.add_argument('--csv', default='insurance.csv')
    parser.add_argument('--database', required=True)
    parser.add_argument('--collection', required=True)
    parser.add_argument('--allow-write', action='store_true',
                        help='Explicitly permit inserts. Re-running may create duplicates.')
    args = parser.parse_args(argv)
    if not args.allow_write:
        parser.error('No database connection made. Review the target and pass --allow-write to insert.')
    uri = os.environ.get('MONGODB_URI', '').strip()
    if not uri:
        parser.error('Set MONGODB_URI locally. Do not commit or paste it into chat.')
    records = read_records(args.csv)
    if not records:
        parser.error('No records found. No database connection made.')
    try:
        from pymongo import MongoClient
    except ImportError:
        parser.error('Optional MongoDB importer requires pymongo, not needed for the app/tests.')
    # Data types remain CSV strings. This is ingestion, not feature preparation.
    try:
        with MongoClient(uri, serverSelectionTimeoutMS=5000) as client:
            result = client[args.database][args.collection].insert_many(records, ordered=True)
        print(f'Inserted {len(result.inserted_ids)} records. No row contents printed.')
    except Exception:
        # Driver errors may include connection details. Do not echo them.
        raise SystemExit('Import failed. Inspect the target privately. Partial inserts may exist; do not retry blindly.') from None


if __name__ == '__main__':
    main()
