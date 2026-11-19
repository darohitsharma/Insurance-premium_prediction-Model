import ast
import importlib.util
import math
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


features = load('features')


class FeatureTests(unittest.TestCase):
    def test_documented_order(self):
        self.assertEqual(features.FEATURES, ('age', 'sex', 'bmi', 'children', 'smoker', 'region'))
        self.assertEqual(features.encode_features(25, 'male', 25, 2, 'yes', 'northeast'), [25, 1, 25.0, 2, 1, 4])

    def test_all_regions(self):
        for label, expected in features.REGION.items():
            self.assertEqual(features.encode_features(18, 'female', 20, 0, 'no', label)[-1], expected)

    def test_invalid_numeric_values(self):
        for index, value in [(0, 17), (0, 25.2), (2, 0), (2, math.inf), (2, math.nan), (3, -1), (3, 1.2), (3, 6)]:
            args = [25, 'female', 25, 0, 'no', 'southwest']
            args[index] = value
            with self.assertRaises(ValueError):
                features.encode_features(*args)

    def test_unknown_categories(self):
        for index in (1, 4, 5):
            args = [25, 'female', 25, 0, 'no', 'southwest']
            args[index] = 'unknown'
            with self.assertRaises(ValueError):
                features.encode_features(*args)


class ImporterTests(unittest.TestCase):
    def test_import_needs_no_database_package_or_network(self):
        with patch('socket.socket', side_effect=AssertionError('Network forbidden')):
            module = load('data_dump')
            self.assertTrue(callable(module.main))

    def test_write_is_explicit(self):
        module = load('data_dump')
        with self.assertRaises(SystemExit):
            module.main(['--database', 'example', '--collection', 'example'])

    def test_missing_uri_denies_before_network(self):
        module = load('data_dump')
        with patch.dict('os.environ', {}, clear=True), self.assertRaises(SystemExit):
            module.main(['--database', 'example', '--collection', 'example', '--allow-write'])

    def test_csv_header_validation(self):
        module = load('data_dump')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'invented.csv'
            path.write_text('wrong,header\nx,y\n')
            with self.assertRaises(ValueError):
                module.read_records(path)

    def test_synthetic_csv(self):
        module = load('data_dump')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'invented.csv'
            path.write_text('age,sex,bmi,children,smoker,region,expenses\n25,female,20,0,no,southwest,100\n')
            self.assertEqual(len(module.read_records(path)), 1)

    def test_current_python_has_no_literal_database_uri(self):
        for path in ROOT.glob('*.py'):
            tree = ast.parse(path.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    self.assertNotIn('mongodb' + '+srv://', node.value)
                    self.assertNotIn('mongodb' + '://', node.value)


if __name__ == '__main__':
    unittest.main()
