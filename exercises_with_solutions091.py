
# coding: utf-8

# # Apple Stock

# ### Introduction:
# 
# We are going to use Apple's stock price.
# 
# 
# ### Step 1. Import the necessary libraries

# In[4]:

import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)

# ### Step 3. Assign it to a variable apple

# In[32]:

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

apple.head()


# ### Step 4.  Check out the type of the columns

# In[33]:

apple.dtypes


# ### Step 5. Transform the Date column as a datetime type

# In[34]:

apple.Date = pd.to_datetime(apple.Date)

apple['Date'].head()


# ### Step 6.  Set the date as the index

# In[35]:

apple = apple.set_index('Date')

apple.head()


# ### Step 7.  Is there any duplicate dates?

# In[36]:

# NO! All are unique
apple.index.is_unique


# ### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.

# In[39]:

apple.sort_index(ascending = True).head()


# ### Step 9. Get the last business day of each month

# In[48]:

apple_month = apple.resample('BM').mean()

apple_month.head()


# ### Step 10.  What is the difference in days between the first day and the oldest

# In[65]:

(apple.index.max() - apple.index.min()).days


# ### Step 11.  How many months in the data we have?

# In[66]:

apple_months = apple.resample('BM').mean()

len(apple_months.index)


# ### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches

# In[81]:

# makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)


# ### BONUS: Create your own question and answer it.

# In[ ]:



