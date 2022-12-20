"""Testing colour_count_by_brand methods"""
import unittest
import os
from apps.colour_count_by_brand import Colour


class TestColourCountByBrand(unittest.TestCase):
    """Test colour_count_by_brand_d() method."""

    def setUp(self):
        """Create colour objects for the four testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.car_stats = Colour(f'{data_dir}/USA_cars_datasets.csv')
        self.car_stats_empty = Colour(f'{data_dir}/car_dataset_empty.csv')
        self.car_stats_five = Colour(f'{data_dir}/car_dataset_5.csv')
        self.car_stats_one = Colour(f'{data_dir}/car_dataset_1.csv')

    def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
        actual_res = self.car_stats.colour_count_by_brand_d()
        print(self.car_stats.brand_colour_d())
        print(actual_res)

    def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
        actual_res1 = self.car_stats_empty.colour_count_by_brand_d()
        print(self.car_stats_empty.brand_colour_d())
        print(actual_res1)
        expected_result = {}
        self.assertDictEqual(actual_res1, expected_result)

    def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
        actual_res2 = self.car_stats_five.colour_count_by_brand_d()
        print(self.car_stats_five.brand_colour_d())
        print(actual_res2)
        expected_result = {'toyota': {'black': 1},
                           'ford': {'silver': 1, 'blue': 1},
                           'dodge': {'silver': 1}, 'chevrolet': {'red': 1}}
        self.assertDictEqual(actual_res2, expected_result)

    def test_one_entries(self):
        """Test case 3 using car_dataset_1.csv."""
        actual_res3 = self.car_stats_one.colour_count_by_brand_d()
        print(self.car_stats_one.brand_colour_d())
        print(actual_res3)
        expected_result = {'toyota': {'black': 1}}
        self.assertDictEqual(actual_res3, expected_result)

