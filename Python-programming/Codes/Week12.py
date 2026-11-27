# Python Pandas' series 

import pandas as pd

# Creating a simple Pandas Series from a list
a = [1, 33, 3]

myvar = pd.Series(a)

print(myvar)

# Creating our own labels
a = [1, 33, 3]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Accessing a item by referring to the label
print(myvar["x"])

# Creating a simple Pandas Series from a dictionary
calories = {"DAY1": 550, "DAY2": 887, "DAY3": 456}

myvar = pd.Series(calories)

print(myvar)

# Creating a Series using only data from "day1" and "day2"
myvar = pd.Series(calories, index = ["DAY1", "DAY2"])

print(myvar)

# Creating a DataFrame from two Series
data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)



# Python Pandas DataFrames

import pandas as pd

# Creating a simple Pandas DataFrame
data = {
    "calories" : [420, 789, 398],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

# Returning row 
print(df.loc[[0, 1]])

# Adding a list of names to give each row a name
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

# Returning "day2"
print(df.loc["day3"])

# Loading a comma separated file (CSV file) into a DataFrame
df = pd.read_csv('data.csv')

print(df)



# Python Pandas Read CSV

import pandas as pd

# Loading the CSV into a DataFrame
df = pd.read_csv('data.csv')

print(df.to_string())

# Printing the DataFrame without the to_string() method
df = pd.read_csv('data.csv')

print(df)

# Checking the number of maximum returned rows
print(pd.options.display.max_rows)


# Increasing the maximum number of rows to display the entire DataFrame
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')

print(df)



# Python Pandas Read Json

import pandas as pd

# Loading the JSON file into a DataFrame
# df = pd.read_json('data.json')

# print(df.to_string())

# Loading a Python Dictionary into a DataFrame
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)



# Program of Python for analyzing dataframes

import pandas as pd

df = pd.read_csv('data.csv')

# Program for quick overview by printing the first 10 rows of the dataframe
print(df.head(10))

# Printing first 5 rows of the dataframe
print(df.head())

# Printing last 5 rows of the dataframe
print(df.tail())


# Info about the data
# Printing information about the data
print(df.info())


