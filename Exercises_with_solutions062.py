
# coding: utf-8

# # Wind Statistics

# ### Introduction:
# 
# The data have been modified to contain some missing values, identified by NaN.  
# Using pandas should make this exercise
# easier, in particular for the bonus question.
# 
# You should be able to perform all of these operations without using
# a for loop or other looping construct.
# 
# 
# 1. The data in 'wind.data' has the following format:

# In[1]:

"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""


#    The first three columns are year, month and day.  The
#    remaining 12 columns are average windspeeds in knots at 12
#    locations in Ireland on that day.   
# 
#    More information about the dataset go [here](wind.desc).

# ### Step 1. Import the necessary libraries

# In[2]:

import pandas as pd
import datetime


# ### Step 2. Import the dataset from this [address](https://github.com/guipsamora/pandas_exercises/blob/master/Stats/Wind_Stats/wind.data)

# ### Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

# In[414]:

# parse_dates gets 0, 1, 2 columns and parses them as the index
data = pd.read_table("wind.data", sep = "\s+", parse_dates = [[0,1,2]]) 
data.head()


# ### Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.

# In[415]:

# The problem is that the dates are 2061 and so on...

# function that uses datetime
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# data.info()
data.head()


# ### Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

# In[1]:

# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])

# set 'Yr_Mo_Dy' as the index
data = data.set_index('Yr_Mo_Dy')

data.head()
# data.info()


# ### Step 6. Compute how many values are missing for each location over the entire record.  
# #### They should be ignored in all calculations below. 

# In[423]:

# "Number of non-missing values for each location: "
data.isnull().sum()


# ### Step 7. Compute how many non-missing values there are in total.

# In[424]:

# number of columns minus the number of missing values for each location
data.shape[1] - data.isnull().sum()


# ### Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
# #### A single number for the entire dataset.

# In[426]:

# print 'Mean over all values is: '
data.mean().mean()


# ### Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
# 
# #### A different set of numbers for each location.

# In[264]:

loc_stats = pd.DataFrame()

loc_stats['min'] = data.min() # min
loc_stats['max'] = data.max() # max 
loc_stats['mean'] = data.mean() # mean
loc_stats['std'] = data.std() # standard deviations

loc_stats


# ### Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# 
# #### A different set of numbers for each day.

# In[404]:

# create the dataframe
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max 
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

day_stats.head()


# ### Step 11. Find the average windspeed in January for each location.  
# #### Treat January 1961 and January 1962 both as January.

# In[427]:

# print "January windspeeds:"

# creates a new column 'date' and gets the values from the index
data['date'] = data.index

# creates a column for each value from date
data['month'] = data['date'].apply(lambda date: date.month)
data['year'] = data['date'].apply(lambda date: date.year)
data['day'] = data['date'].apply(lambda date: date.day)

# gets all value from the month 1 and assign to janyary_winds
january_winds = data.query('month == 1')

# gets the mean from january_winds, using .loc to not print the mean of month, year and day
january_winds.loc[:,'RPT':"MAL"].mean()


# ### Step 12. Downsample the record to a yearly frequency for each location.

# In[428]:

data.query('month == 1 and day == 1')


# ### Step 13. Downsample the record to a monthly frequency for each location.

# In[429]:

data.query('day == 1')


# ### Step 14. Downsample the record to a weekly frequency for each location.

# In[430]:

data[::7].head()


# ### Step 15. Calculate the mean windspeed for each month in the dataset.  
# #### Treat January 1961 and January 1962 as *different* months.
# #### (hint: first find a  way to create an identifier unique for each month.)

# In[3]:

# call data again but this time don't use parse_dates
wind_data = pd.read_table("wind.data", sep = "\s+") 

# compute the month number for each day in the dataset, there are in total 216 months
wind_data['months_num'] = (wind_data.iloc[:, 0] - 61) * 12 + wind_data.iloc[:, 1]

wind_data

# group the data according to the months_num and get the mean
# monthly_data = wind_data.groupby(['months_num']).mean()

# monthly_data.head()


# ### Step 16. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

# In[433]:

# resample data to 'W' week and use the functions
weekly = data.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.ix[1:53, "RPT":"MAL"].head(10)

