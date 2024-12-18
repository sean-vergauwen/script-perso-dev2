import unittest
import pandas as pd
import tempfile
import os
from src.data_import import import_csv_files


class TestDataImport(unittest.TestCase):
    def setUp(self):
        # Create temporary CSV files for testing
        self.temp_dir = tempfile.mkdtemp()
        self.test_file1 = os.path.join(self.temp_dir, "test1.csv")
        self.test_file2 = os.path.join(self.temp_dir, "test2.csv")

        # Create test data
        pd.DataFrame({
            'category': ['A', 'B'],
            'quantity': [1, 2],
            'unit_price': [10.0, 20.0]
        }).to_csv(self.test_file1, index=False)

        pd.DataFrame({
            'category': ['C', 'D'],
            'quantity': [3, 4],
            'unit_price': [30.0, 40.0]
        }).to_csv(self.test_file2, index=False)

    def tearDown(self):
        # Clean up temporary files
        for file in [self.test_file1, self.test_file2]:
            if os.path.exists(file):
                os.remove(file)
        os.rmdir(self.temp_dir)

    def test_import_csv_files_success(self):
        data_frames = import_csv_files([self.test_file1, self.test_file2])
        self.assertEqual(len(data_frames), 2)
        self.assertEqual(len(data_frames[0]), 2)
        self.assertEqual(len(data_frames[1]), 2)

    def test_import_csv_files_nonexistent(self):
        data_frames = import_csv_files(['nonexistent.csv'])
        self.assertEqual(len(data_frames), 0)