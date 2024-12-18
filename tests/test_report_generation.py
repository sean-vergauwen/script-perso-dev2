import unittest
import pandas as pd
import os
from src.report_generation import generate_report

class TestReportGeneration(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        self.test_file = 'test_inventory.csv'
        pd.DataFrame({
            'category': ['A', 'A', 'B'],
            'quantity': [1, 2, 3],
            'unit_price': [10.0, 10.0, 20.0]
        }).to_csv(self.test_file, index=False)
        self.output_path = '../outputs/report.csv'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_generate_report_success(self):
        report = generate_report(self.test_file)
        self.assertIsNotNone(report)
        self.assertEqual(len(report), 2)  # Should have 2 categories
        self.assertTrue(os.path.exists(self.output_path))

    def test_generate_report_calculations(self):
        report = generate_report(self.test_file)
        category_a = report[report['category'] == 'A'].iloc[0]
        self.assertEqual(category_a['total_quantity'], 3)  # 1 + 2
        self.assertEqual(category_a['total_value'], 30.0)  # (1 * 10) + (2 * 10)

    def test_generate_report_file_not_found(self):
        report = generate_report('nonexistent.csv')
        self.assertIsNone(report)