
# coding: utf-8

# # United States - Crime Rates - 1960 - 2014

# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[95]:

import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 

# ### Step 3. Assign it to a variable called crime.

# In[265]:

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()


# ### Step 4. What is the type of the columns?

# In[266]:

crime.info()


# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

# In[267]:

# pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()


# ### Step 6. Set the Year column as the index of the dataframe

# In[268]:

crime = crime.set_index('Year', drop = True)
crime.head()


# ### Step 7. Delete the Total column

# In[269]:

del crime['Total']
crime.head()


# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

# In[270]:

# To learn more about .resample (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)
# To learn more about Offset Aliases (http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases)

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

crimes


# ### Step 9. What is the mos dangerous decade to live in the US?

# In[276]:

# apparently the 90s was a pretty dangerous time in the US
crime.idxmax(0)

