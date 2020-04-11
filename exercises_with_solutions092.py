
# coding: utf-8

# # Getting Financial Data - Google Finance

# ### Introduction:
# 
# This time you will get data from a website.
# 
# 
# ### Step 1. Import the necessary libraries

# In[30]:

import pandas as pd

# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb

# package for dates
import datetime as dt


# ### Step 2. Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is)

# In[75]:

start = dt.datetime(2015, 1, 1)

end = dt.datetime.today()

start


# ### Step 3. Select the Apple, Tesla, Twitter, IBM, LinkedIn stocks symbols and assign them to a variable called stocks

# In[76]:

stocks = ['AAPL', 'TSLA', 'IBM', 'LNKD']


# ### Step 4. Read the data from google, assign to df and print it

# In[77]:

df = web.DataReader(stocks, 'google', start, end)
df


# ### Step 5.  What is the type of structure of df ?

# In[ ]:

# 'pandas.core.panel.Panel'


# ### Step 6. Print all the Items axis values
# #### To learn more about the Panel structure go to [documentation](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panel) 

# In[120]:

df.items


# ### Step 7. Good, now we know  the data avaiable. Create a dataFrame called vol, with the Volume values.

# In[122]:

vol = df['Volume']
vol.head()


# ### Step 8. Aggregate the data of Volume to weekly
# #### Hint: Be careful to not sum data from the same week of 2015 and other years.

# In[132]:

vol['week'] = vol.index.week
vol['year'] = vol.index.year

week = vol.groupby(['week','year']).sum()
week.head()


# ### Step 9. Find all the volume traded in the year of 2015

# In[131]:

del vol['week']
vol['year'] = vol.index.year

year = vol.groupby(['year']).sum()
year


# ### BONUS: Create your own question and answer it.

# In[ ]:



