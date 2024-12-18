import unittest
import pandas as pd
import os
from src.data_processing import consolidate_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.df1 = pd.DataFrame({
            'category': ['A', 'B'],
            'quantity': [1, 2],
            'unit_price': [10.0, 20.0]
        })
        self.df2 = pd.DataFrame({
            'category': ['B', 'C'],
            'quantity': [2, 3],
            'unit_price': [20.0, 30.0]
        })
        self.test_output_path = '../outputs/consolidated_inventory.csv'

    def test_consolidate_data_success(self):
        consolidate_data([self.df1, self.df2])
        self.assertTrue(os.path.exists(self.test_output_path))
        result = pd.read_csv(self.test_output_path)
        self.assertEqual(len(result), 3)  # Should have 3 unique rows after deduplication
