# DESIGN DOCUMENT
Authors:1.Prudhvi.
        2.Mohamed,
        3.Vestine
Date: 11/30/2022
## Investigative Question 1:
What is the average selling price of a particular car brand?
* The inputs are Brand and Selling price which are second and third columns in the data set.
* the input is dictionary inp_d with key as brand and value as list of selling price.
* We are going to use `average_selling_price` method.
* An accumulator called `temp1` is used to get the sum of selling price.
* An accumulator called `temp2` is used to get the count, it is initialized with 0.
* for loop is used to create the sum by iterating through the list.
* Get average selling prize by diving temp1 and temp2.
* the output will dictionary out_d with brand as key and selling price as value.

## Investigative Question 2:
What is the count of a particular colour car sold by a particular brand?
* The inputs are Brand and Selling price which are second and third columns in the data set.
* We are going to use `car_colour` method.
* Using a for loop we will iterate through the dictionary called `input_d` and check for the brand.
* Using the internal for loop we can get the number of cars per colour in a particular brand using the accumulator `Colour_d` which is initialized to an empty dictionary.
* the input is dictionary inp_d with key as `brand` and value as `colour`.
* the output will dictionary out_d with `brand` as key and Dictionary as value.The internal dictionary contains `colours` as key and `count of cars` as value.

## Investigative Question 3:
What is the number of cars sold in a state?.
* The input is State.
* We are going to use `car_state` method.
* Using an if else statement we check weather the particular car is sold in that state, if that statement is true then the value in `state_d` is incremented. 
* Input is the `list of states`
* output is Dictionary with key as `city` and `count of cars sold` as value.
* Input is the list of states
* output is Dictionary with key as city and count of cars sold as value.
[12:04 AM]
copy this in DESIGN.md
[12:04 AM]
and push in your branch


