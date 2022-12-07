"""
count_by_state.py
Developer: vestine
Last updated: 12/7/2022
"""

import csv


class CarsSold:
    """
    Data processing functionality
    Attributes:
        filename: string
    """
    def __init__(self, filename):
        """
        Instance variable initialization
        :param filename: string
        """
        self.filename = filename

    def file_to_list(self, value: int) -> list:
        """
        Reads from csv file named self. filename using csv.reader() method
        and creates a list with the values in the list
        :param value: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: List of all the state
        """
        car_dict = []
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:
                    key = row[value]
                    car_dict.append(key)
        return car_dict

    @property
    def count_by_state_l(self):
        """
        Creates and returns a list which represents states in USA
        :return: List of strings which represents states in usa.
        """
        state_idx = 10
        date_by_voting_average_d = self.file_to_list(state_idx)
        return date_by_voting_average_d

    def count_of_sold_cars_by_state(self):
        """
        Creates and returns a new dictionary whose keys are state names
            and values are count of cars sold in that state
        :returns: dictionary
           key: str, state
           value: int, Count of cars sold.
        """

        state_dict = {}
        state_list = self.count_by_state_l
        for a_state in state_list:
            if a_state in state_dict:
                state_dict[a_state] += 1
            else:
                state_dict[a_state] = 1
        return state_dict
