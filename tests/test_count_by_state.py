"""Testing count_by_state methods."""
import unittest
import os
from apps.count_by_state import CarsSold


class TestSoldCarCountByState(unittest.TestCase):
    """Testing count_of_sold_cars_by_state."""

    def setUp(self):
        """Create cars sold objects for the four testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.car_stats = CarsSold(f'{data_dir}/USA_cars_datasets.csv')
        self.car_stats_empty = CarsSold(f'{data_dir}/car_dataset_empty.csv')
        self.car_stats_five = CarsSold(f'{data_dir}/car_dataset_5.csv')
        self.car_stats_one = CarsSold(f'{data_dir}/car_dataset_1.csv')

    def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
        actual_res = self.car_stats.count_of_sold_cars_by_state()
        print(self.car_stats.count_by_state_l)
        print(actual_res)

    def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
        actual_res1 = self.car_stats_empty.count_of_sold_cars_by_state()
        print(self.car_stats_empty.count_by_state_l)
        print(actual_res1)
        expected_result = {}
        self.assertDictEqual(actual_res1, expected_result)

    def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
        actual_res2 = self.car_stats_five.count_of_sold_cars_by_state()
        print(self.car_stats_five.count_by_state_l)
        print(actual_res2)
        expected_result = {'new jersey': 1, 'tennessee': 1,
                           'georgia': 1, 'virginia': 1, 'florida': 1}
        self.assertDictEqual(actual_res2, expected_result)

    def test_one_entries(self):
        """Test case 3 using car_dataset_1.csv."""
        actual_res3 = self.car_stats_one.count_of_sold_cars_by_state()
        print(self.car_stats_one.count_by_state_l)
        print(actual_res3)
        expected_result = {'new jersey': 1}
        self.assertDictEqual(actual_res3, expected_result)
