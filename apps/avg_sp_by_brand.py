"""
avg_sp_by_brand.py
Developer: Mohamed
Last updated: 12/7/2022
"""

import csv


class BrandPrice:
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

    def file_to_dictionary(self, key_column: int, value_column: int) -> dict
        [str, list[int]]:
        """
        Reads from text file named self. filename using csv.reader() method
        and creates a dictionary with the data in column key_column as keys and
        data in column value_column as values
        :param key_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing brand in column key_file
            value: List of int values corresponding values in column value_column
        """



    def brand_by_price_d(self):
        """
        Creates and returns a dictionary whose keys are brands of cars
        and values are list of their selling prices.
        :return: dictionary
            key: str, representing brand name
            value: list of integers, representing selling prices of cars
        """


    def average_selling_price_by_brand(self) -> dict[str, float]:
        """
        Gets dictionary of brand name and list of selling prices by calling
            self.brand_by_price_d().
        Creates and returns a new dictionary whose keys are brand names
            and value is average selling price of corresponding brand.
        :returns: dictionary
           key: str, Brand
           value: Float, Average selling price of corresponding brand car.
        """


