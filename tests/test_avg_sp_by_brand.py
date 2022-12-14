"""Testing Average selling price methods."""
import unittest
import os
from apps.avg_sp_by_brand import BrandPrice


class TestAverageSellingPrice(unittest.TestCase):
    """Test average_selling_price_by_brand() method."""

    def setUp(self):
        """Create Brand Price objects for the four testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.car_stats = BrandPrice(f'{data_dir}/USA_cars_datasets.csv')
        self.car_stats_empty = BrandPrice(f'{data_dir}/car_dataset_empty.csv')
        self.car_stats_five = BrandPrice(f'{data_dir}/car_dataset_5.csv')
        self.car_stats_one = BrandPrice(f'{data_dir}/car_dataset_1.csv')

    def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
        actual_res = self.car_stats.average_selling_price_by_brand()
        print(self.car_stats.brand_by_price_d())
        print(actual_res)

    def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
        actual_res1 = self.car_stats_empty.average_selling_price_by_brand()
        print(self.car_stats_empty.brand_by_price_d())
        print(actual_res1)
        expected_result = {}
        self.assertDictEqual(actual_res1, expected_result)

    def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
        actual_res2 = self.car_stats_five.average_selling_price_by_brand()
        print(self.car_stats_five.brand_by_price_d())
        print(actual_res2)
        expected_result = {'toyota': 6300.0, 'ford': 13949.5,
                           'dodge': 5350.0, 'chevrolet': 27700.0}
        self.assertDictEqual(actual_res2, expected_result)

    def test_one_entries(self):
        """Test case 3 using car_dataset_1.csv."""
        actual_res3 = self.car_stats_one.average_selling_price_by_brand()
        print(self.car_stats_one.brand_by_price_d())
        print(actual_res3)
        expected_result = {'toyota': 6300.0}
        self.assertDictEqual(actual_res3, expected_result)
