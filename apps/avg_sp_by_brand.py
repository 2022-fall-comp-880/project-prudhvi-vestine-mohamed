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

    def __init__(self, filename: str) -> None:
        """
        Instance variable initialization
        :param filename: string
        """
        self.filename = filename

    def file_to_dictionary(self, key_column: int, value_column: int) \
    -> dict[str, list[int]]:
        """
        Reads from csv file named self. filename using csv.reader() method
        and creates a dictionary with the data in column key_column as keys and
        data in column value_column as values
        :param key_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing brand in column key_file
            value: List of int values corresponding values in column
            value_column
        """
        car_dict = {}
        with open(self.filename, encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for count, row in enumerate(reader):
                if count != 0:
                    key = row[key_column]
                    value = int(row[value_column])
                    if key in car_dict:
                        car_dict[key].append(value)
                    else:
                        car_dict[key] = [value]
        return car_dict

    def brand_by_price_d(self) -> dict[str, list[int]]:
        """
        Creates and returns a dictionary whose keys are brands of cars
        and values are list of their selling prices.
        :return: dictionary
            key: str, representing brand name
            value: list of integers, representing selling prices of cars
        """
        brand_idx = 2
        price_idx = 1
        brand_by_price = self.file_to_dictionary(brand_idx, price_idx)
        return brand_by_price

    def average_selling_price_by_brand(self) -> dict[str, float]:
        """
        Gets dictionary of brand name and list of selling prices by calling
            self.brand_by_price_d().
        Creates and returns a new dictionary whose keys are brand names
            and value is average selling price of corresponding brand.
        :returns: dictionary
           key: str, Brand name
           value: Float, Average selling price of corresponding brand car.
        """
        brand_dict = self.brand_by_price_d()
        brand_avg_sp_dict = {}
        for brand, prices_list in brand_dict.items():
            sum_prices = 0
            count = 0
            for price in prices_list:
                sum_prices += price
                count += 1
            brand_avg_sp_dict[brand] = round(sum_prices / count, 2)

        return brand_avg_sp_dict
