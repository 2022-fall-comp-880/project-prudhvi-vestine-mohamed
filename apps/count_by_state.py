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

    def init(self, filename):
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

    @property
    def count_by_state(self):
        """
        Creates and returns a list which represents states in USA
        :return: List of strings which represents states in usa.
        """

    def count_of_sold_cars_by_state(self):
        """
        Creates and returns a new dictionary whose keys are state names
            and values are count of cars sold in that state
        :returns: dictionary
           key: str, state
           value: int, Count of cars sold.
        """
