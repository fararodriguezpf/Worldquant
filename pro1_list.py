# python comes with several data structures that can be used to organize tabular data. let's start by putting a single observation in a list

# declare variable 'house_0_list'
house_0_list = [11591.25, 128, 4]

"""
at the end, you will be able to answer the following questions:
what is a list?
access an item in a list using python
perform basic mathematical operations in python

"""

# declare a variable 'house_0_price_m2'
house_0_price_m2 = house_0_price_m2 / house_0_list[1]

# append price/sq. meter to 'house_0_list
house_0_list.append(house_0_price_m2)

#now that you can work with data for a single house, let's think about how to organize the whole dataset. one option would be to create a list for each observation and then put those together in another list. this is called nested list

# declare a variable 'houses_nested_list'
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

# now that we have more observations, it doesn't make sense to calculate the price per square meter for each house one-by-one. instead, we can automate this repetitive task using a for loop

"""
at the end, you will be able to answer the following questions:
what is a for loop?
write a for loop in python
"""

# create for loop to iterate through "houses_nested_list"
for house in houses_nested_list:
  # for each observation, append price / sq. meter
  price_m2 = house[0] / house[1]
  house.append(price_m2)

# WORKING WITH DICTIONARIES
"""
lists are a good way to organize data, but one drawback is that we can only represent values. why is that a problem
for example someone looking at [115910.26, 128.0, 4] wouldn't know which values correspond to price, area etc. a 
better option might be a dictionary, where each value is associated with a key. here's what house_0 looks
like as a dictionary instead of a list
"""

# declare variable 'house_0_dict'
house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

# Print `house_0_dict` type
print("house_0_dict type:", type(house_0_dict))

# Get output of `house_0_dict`
house_0_dict

"""
at the end, you will be able to answer the following:
what is a dictionary?
access an item in a dictionary in python
"""

# add 'price_per_m2" key-value pair to 'house_0_dict'
house_0_dict['price_per_m2'] = house_0_dict["price_approx_usd'] / house_0_dict["surface_covered_in_m2"]

# if we wanted to combine all our observations together, the best way would be to create a list of dictionaries

houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]

"""
task : using a for loop, calculate the price per square meter and store the result under a 'price_per+m2" key for each observation in houses_rowwise
what is json
"""

# create for loop to iterate through 'houses_rowwise'
for house in houses_rowwise:
  # for each observation, add 'price_per_m2' key-value pair
  house["price_per_m2"] = house["price_approx_usd"] / house["surface_covered_in_m2"]

#task : to calculate the mean price for houses_rowwise 

# declare 'house_prices' as empty list
house_prices = [ ]

# iterate through 'houses_rowwise'
for house in houses_rowwise:
  house_prices.append(house["price_approx_usd"])
  # for each house, append "price_approx_usd" to 'house_prices'

# calculate 'mean_house_price' using 'house_prices'
mean_house_price = sum(house_prices) / len(house_prices)


""" 
task : 
add a key-value pair to a dictionary in python
zip two lists together in python
write a for loop in python
"""

price = houses_columnwise["price_approx_usd"]
area = houses_columnwise["surface_covered_in_m2"]
price_per_m2 = []

for p,a in zip(price,area):
    price_m2 = p/a
    price_per_m2.append("price m_2")

# add "price_per_m2" key-value pair for 'houses_columnwise'

import pandas as pd

# Declare variable 'df_houses'
df_houses = pd.DataFrame(houses_columnwise
houses_columnwise["price_per_m2"]
