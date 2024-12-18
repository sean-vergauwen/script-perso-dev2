import unittest
import pandas as pd
import os
from src.data_query import query_data

class TestDataQuery(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        self.test_file = 'test_inventory.csv'
        pd.DataFrame({
            'category': ['A', 'B', 'C'],
            'quantity': [1, 2, 3],
            'unit_price': [10.0, 20.0, 30.0]
        }).to_csv(self.test_file, index=False)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_query_data_success(self):
        result = query_data(self.test_file, 'quantity > 1')
        self.assertEqual(len(result), 2)
        self.assertTrue(all(result['quantity'] > 1))

    def test_query_data_no_matches(self):
        result = query_data(self.test_file, 'quantity > 10')
        self.assertEqual(result, None)

    def test_query_data_file_not_found(self):
        result = query_data('nonexistent.csv', 'quantity > 1')
        self.assertIsNone(result)
