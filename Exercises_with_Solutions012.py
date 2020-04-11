
# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[2]:

users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')


# ### Step 4. See the first 25 entries

# In[3]:

users.head(25)


# ### Step 5. See the last 10 entries

# In[4]:

users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[5]:

users.shape[0]


# ### Step 7. What is the number of columns in the dataset?

# In[6]:

users.shape[1]


# ### Step 8. Print the name of all the columns.

# In[7]:

users.columns


# ### Step 9. How is the dataset indexed?

# In[8]:

# "the index" (aka "the labels")
users.index


# ### Step 10. What is the data type of each column?

# In[9]:

users.dtypes


# ### Step 11. Print only the occupation column

# In[10]:

users.occupation 

#OR

users['occupation']


# ### Step 12. How many different occupations there are in this dataset?

# In[14]:

users.occupation.nunique()


# ### Step 13. What is the most frequent occupation?

# In[15]:

users.occupation.value_counts().head()


# ### Step 14. Summarize the DataFrame.

# In[16]:

users.describe() #Notice is only the numeric column


# ### Step 15. Summarize all the columns

# In[17]:

users.describe(include = "all") #Notice is only the numeric column


# ### Step 16. Summarize only the occupation column

# In[18]:

users.occupation.describe()


# ### Step 17. What is the mean age of users?

# In[19]:

round(users.age.mean())


# ### Step 18. What is the age with least occurrence?

# In[20]:

users.age.value_counts().tail(1) #7 years, only 1 occurrence

