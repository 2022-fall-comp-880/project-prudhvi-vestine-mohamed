"""
colour_count_by_brand.py
Developer: Prudhvi Krishna
Last updated: 12/7/2022
"""

import csv


class Colour:
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

    def file_to_dictionary(self, key_column, value_column):
        """
        Reads from text file named self.filename using csv.reader() method
        and creates a dictionary with the data in column key_column as keys and
        data in column value_column as values
        :param key_column:non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_column:non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing data points in column key_file
            value: list of strings of corresponding values in column value_file
        """
        car_dict = {}
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:
                    key = row[key_column]
                    value = row[value_column]
                    if key in car_dict:
                        car_dict[key].append(value)
                    else:
                        car_dict[key] = [value]
        return car_dict

    def brand_colour_d(self):
        """
        Creates and returns a dictionary whose keys are brand names and
        values are list of colours
        :return: dictionary
            key: str, representing brand name
            value: list of strings, car colour
        """
        brand_idx = 2
        colour_idx = 7
        brand_by_colour = self.file_to_dictionary(brand_idx, colour_idx)
        return brand_by_colour

    def colour_count_by_brand_d(self):
        """
        Creates and returns a new dictionary whose keys brand names
        and values are dictionaries where keys are car colours and corresponding counts as values
        :returns: dictionary
           key: str, brand
           value: dictionary, keys as colours and values as count of particular colour cars.
        """
        brand_colour_dict = self.brand_colour_d()
        brand_colour_count = {}
        for brand, colour_list in brand_colour_dict.items():
            colour_dict = {}
            for a_colour in colour_list:
                if a_colour in colour_dict:
                    colour_dict[a_colour] += 1
                else:
                    colour_dict[a_colour] = 1
            brand_colour_count[brand] = colour_dict
        return brand_colour_count


