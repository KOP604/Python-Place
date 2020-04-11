
# coding: utf-8

# # Investor - Flow of Funds - US

# ### Introduction:
# 
# Special thanks to: https://github.com/rgrp for sharing the dataset.
# 
# ### Step 1. Import the necessary libraries

# In[30]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv). 

# ### Step 3. Assign it to a variable called 

# In[31]:

url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
df.head()


# ### Step 4.  What is the frequency of the dataset?

# In[32]:

# weekly data


# ### Step 5. Set the column Date as the index.

# In[33]:

df = df.set_index('Date')
df.head()


# ### Step 6. What is the type of the index?

# In[34]:

df.index
# it is a 'object' type


# ### Step 7. Set the index to a DatetimeIndex type

# In[35]:

df.index = pd.to_datetime(df.index)
type(df.index)


# ### Step 8.  Change the frequency to monthly, sum the values and assign it to monthly.

# In[36]:

monthly = df.resample('M').sum()
monthly


# ### Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.

# In[37]:

monthly = monthly.dropna()
monthly


# ### Step 10. Good, now we have the monthly data. Now change the frequency to year.

# In[38]:

year = monthly.resample('AS-JAN').sum()
year


# ### BONUS: Create your own question and answer it.

# In[ ]:



