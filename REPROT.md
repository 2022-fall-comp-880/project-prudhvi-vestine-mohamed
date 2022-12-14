
# Project Report

## 1. Purpose 


* This Project is about the branded cars that are placed in an auction in US. This project helps the buyers and sellers to find the average selling price, Cars sold and briefing about the count of particular colour cars.
* For the project `US CAR AUCTION` we have used `Car auction data`.
  - The source for this project is `https://www.kaggle.com/datasets/doaaalsenani/usa-cers-dataset`.
  - Author of this dataset is `DOAA ALSENANI`.
  - The dataset is last updated 3 years ago.
  - This dataset included Information about 28 brands of clean and used vehicles for sale in US. Twelve features were assembled for each car in the dataset.
  - Price - The sale price of the vehicle in the ad
  - Years - The vehicle registration year
  - Brand - The brand of car
  - Model - model of the vehicle
  - Color - Color of the vehicle
  - State/City - The location in which the car is being available for purchase
  - Mileage -	miles traveled by vehicle
  - Vin - The vehicle identification number is a collection of 17 characters (digits and capital letters)
  - Title Status - This feature included binary classification, which are clean title vehicles and salvage insurance
  - Lot - A lot number is an identification number assigned to a particular quantity or a lot of material from a single manufacturer.For cars, a lot number is combined with a serial number to form the Vehicle Identification Number.
  - Condition -	Time
* We have worked on the below investigative questions.
  - *What is the average selling price of a particular car model?*
  - *What is the number of cars sold in a state?*
  - *What is the count of a particular colour car sold by a particular brand?*
--------------------------------------------------------------------------------------------------------


## 2. Approach 


* We have created a python file for every investigative question and placed them in the src directory.
* The dataset is in the form of csv, so we have imported csv reader for reading the file.
* For every investigative question we have created a method to read the column names that will be used in transformation.
* For each investigative question we have created file_to_collection method to read the data from the data.

### 2.1 Avg Selling Price

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

### 2.2 Count of Cars sold per state.

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

### 2.3 Colour Count by Brand

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
------------------------------------------------------------------------------------------------------------------------


## 3. Testing 


* We have created a test file for every investigative question.
* For every test file we have created three scenarios to test the code along with actual dataset.
  * Testing will actual dataset.
  * Testing with empty dataset.
  * Testing with one entry in the data file.
  * Testing with five entries in the data file.
* We have imported unittest library for testing the project results.

### 3.1 class TestAverageSellingPrice
    """Test average_selling_price_by_brand() method."""
* For every test method we have used assertion statements to validate the 
results. 
#### 3.1.1 def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
* This method takes the whole dataset.
* Output will be a dictionary of all entries in the dataset.
#### 3.1.2 def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
* This method takes the empty dataset.
* Output will be an empty dictionary.
#### 3.1.3 def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
* This method takes the file with five entries.
* Output will be a dictionary of five entries.
#### 3.1.4 def test_one_entries(self):
        """Test case 4 using car_dataset_1.csv."""
* This method takes the file with single entry.
* Output will be a dictionary of single entry.
-------------------------------------------------------------------------------------


### 3.2 class TestSoldCarCountByState
    """Test count_of_sold_cars_by_state() method."""
* For every test method we have used assertion statements to validate the 
results. 
#### 3.2.1 def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
* This method takes the whole dataset.
* Output will be a dictionary of all entries in the dataset.
#### 3.2.2 def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
* This method takes the empty dataset.
* Output will be an empty dictionary.
#### 3.2.3 def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
* This method takes the file with five entries.
* Output will be a dictionary of five entries.
#### 3.2.4 def test_one_entries(self):
        """Test case 4 using car_dataset_1.csv."""
* This method takes the file with single entry.
* Output will be a dictionary of single entry.
-------------------------------------------------------------------------------


### 3.3 class TestColourCountByBrand
    """Test colour_count_by_brand_d() method."""
* For every test method we have used assertion statements to validate the 
results. 
#### 3.3.1 def test_multiple_entries(self):
        """Test case 1 using USA_cars_datasets.csv."""
* This method takes the whole dataset.
* Output will be a dictionary of all entries in the dataset.
#### 3.3.2 def test_empty(self):
        """Test case 2 using car_dataset_empty.csv."""
* This method takes the empty dataset.
* Output will be an empty dictionary.
#### 3.3.3 def test_five_entries(self):
        """Test case 3 using car_dataset_5.csv."""
* This method takes the file with five entries.
* Output will be a dictionary of five entries.
#### 3.3.4 def test_one_entries(self):
        """Test case 4 using car_dataset_1.csv."""
* This method takes the file with single entry.
* Output will be a dictionary of single entry.
---------------------------------------------------------------------------------------------------------------


## 4. Results 

### 4.1 Average Selling price by Brand.
* average_selling_price_by_brand(self) -> dict[str, float]:  
* Output: dictionary (key: str, Brand name)(value: Float, Average selling price of corresponding brand car).

### 4.2 Count of cars sold per state.
* count_of_sold_cars_by_state(self) -> dict[str, int]:
* Output: dictionary(key: str, state)(value: int, Count of cars sold).

### 4.3 Colour count by Brand.
* colour_count_by_brand_d(self) -> dict[str, dict[str, int]]:
* Output: dictionary (key: str, brand)(value: dictionary, keys as colours and 
values as count of particular colour cars).

## 5. Evaluation 



### 5.1 What Works and Scope Assumptions
* Every transformation and Accumulation pattern, 
We have performed in our project worked. We have found average selling price
of each brand, Count of cars sold per state,and Count of cars of each colour
by brand  there the possibility for larger scope by using all fields the data set.
* There is scope for filtering the cars with `no-colour`. We have used only few
fields in the dataset. By using the remaining attributes we can perform many 
transformations on this dataset.

### 5.2 Immediate Further Development 
* Our immediate development would be creating a lookup for a particular brand 
and retrieving the average selling price and count of cars sold by that 
particular brand with all the colour.
