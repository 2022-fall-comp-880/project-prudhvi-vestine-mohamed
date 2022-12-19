# COMP 880 Integrated Practicum
## Car Auction in US 
### DESIGN Document
### Authors: Prudhvi, Mohamed and Vestine.

Date: 11/30/2022


## Investigative Question 1:
**What is the average selling price of a particular car brand?**

class BrandPrice:
    
    Data processing functionality
    Attributes:
        filename: string
def __init__(self, filename: str) -> None:
        
        Instance variable initialization
        :param filename: string
def file_to_dictionary(self, key_column: int, value_column: int) -> dict[str, list[int]]:
        
        Reads from csv file named self. filename using csv.reader() method
        and creates a dictionary with the data in column key_column as keys and
        data in column value_column as values
        :param key_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_column: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing brand in column key_file
            value: List of int values corresponding values in column value_column
def brand_by_price_d(self) -> dict[str, list[int]]:
        
        Creates and returns a dictionary whose keys are brands of cars
        and values are list of their selling prices.
        :return: dictionary
            key: str, representing brand name
            value: list of integers, representing selling prices of cars
def average_selling_price_by_brand(self) -> dict[str, float]:
        
        Gets dictionary of brand name and list of selling prices by calling
            self.brand_by_price_d().
        Creates and returns a new dictionary whose keys are brand names
            and value is average selling price of corresponding brand.
        :returns: dictionary
           key: str, Brand name
           value: Float, Average selling price of corresponding brand car.

* Initialize and empty dictionary to the variable `brand_avg_sp_dict` which will be the accumulator
* Using for loop iterate on `brand_dict.items()` by using iterables `brand` and `price_list`.
  * Iterate on the `price_list` using `price` and initialize `sum_prices` and `count` to 0.
  * For every iteration calculate the sum_prices by add it the price in the price_list.
  * Increment the count value by 1 for every iteration.
  * Calculate average selling price by dividing it with sum_prices and count and round the value to 2 decimal points.
* Assign average selling price as value to `brand_avg_sp_dict` with key as `brand`.
* Return `brand_avg_sp_dict`.

## Investigative Question 2:
**What is the count of a particular colour car sold by a particular brand?**

class Colour:
    
    Data processing functionality
    Attributes:
        filename: string
def __init__(self, filename: str) -> None:
        
        Instance variable initialization
        :param filename: string
def file_to_dictionary(self,
                           key_column: int,
                           value_column: int) -> dict[str, list]:
        
        Reads from text file named self.filename using csv.reader() method
        and creates a dictionary with the data in column key_column as keys and
        data in column value_column as values
        :param key_column:non-negative integer, position of column in the
            text file, with the first column at position 0
        :param value_column:non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: dictionary
            key: string, representing data points in colmn key_file
            value: list of strings of corresponding values in column value_file
def brand_colour_d(self) -> dict[str, list]:
       
        Creates and returns a dictionary whose keys are brand names and
        values are list of colours
        :return: dictionary
            key: str, representing brand name
            value: list of strings, car colour
def colour_count_by_brand_d(self) -> dict[str, dict[str, int]]:
        
        Creates and returns a new dictionary whose keys brand names
        and values are dictionaries where keys are car colours and corresponding counts as values
        :returns: dictionary
           key: str, brand
           value: dictionary, keys as colours and values as count of particular colour cars.
        

* Initialize and empty dictionary to the variable `brand_colour_count` which will be the accumulator
* Using for loop iterate on `brand_colour_dict.items()` by using iterables `brand` and `colour_list`.
  * Initialize and empty dictionary to the variable `colour_dict`.
  * Using for loop iterate on `colour_list` by using iterables `a_color`.
    * If  `a_color` is not in the `colour_list` then assign the value of dictionary `colour_dict` as 1
    * Else increment the value of dictionary `colour_dict` by 1.
  * Return the `colour_dict` as the value to `brand_colour_count` with key as `brand`.
* Return `brand_colour_count`

## Investigative Question 3:

*What is the number of cars sold in a state?*

class CarsSold:
    
    Data processing functionality
    Attributes:
        filename: string
def __init__(self, filename):
        
        Instance variable initialization
        :param filename: string
def file_to_list(self, value: int) -> list[str]:
        
        Reads from csv file named self. filename using csv.reader() method
        and creates a list with the values in the list
        :param value: non-negative integer, position of column in the
            text file, with the first column at position 0
        :return: List of all the state
def count_by_state_l(self) -> list:
       
        Creates and returns a list which represents states in USA
        :return: List of strings which represents states in usa.
def count_of_sold_cars_by_state(self) -> dict[str, int]:
        
        Creates and returns a new dictionary whose keys are state names
            and values are count of cars sold in that state
        :returns: dictionary
           key: str, state
           value: int, Count of cars sold.

        
        
* Initialize and empty dictionary to the variable `state_dict`.
  * Using for loop iterate on `state_list` by using iterables `a_state`.
    * If  `a_state` is not in the `state_list` then assign the value of dictionary `state_dict` as 1
    * Else increment the value of dictionary `state_dict` by 1.
  * Return the `state_dict`.


