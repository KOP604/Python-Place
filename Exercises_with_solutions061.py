
# coding: utf-8

# # US - Baby Names

# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

# In[2]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv). 

# ### Step 3. Assign it to a variable called baby_names.

# In[3]:

baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()


# ### Step 4. See the first 10 entries

# In[4]:

baby_names.head(10)


# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

# In[106]:

# deletes Unnamed: 0
del baby_names['Unnamed: 0']

# deletes Unnamed: 0
del baby_names['Id']

baby_names.head()


# ### Step 6. Is there more male or female names in the dataset?

# In[114]:

baby_names['Gender'].value_counts('F')


# ### Step 7. Group the dataset by name and assign to names

# In[116]:

# you don't want to sum the Year column, so you delete it
# del baby_names["Year"]

# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
names.head()

# print the size of the dataset
print names.shape

# sort it from the biggest value to the smallest one
names.sort_values("Count", ascending = 0).head()


# ### Step 8. How many different names exist in the dataset?

# In[89]:

# as we have already grouped by the name, all the names are unique already. 
# get the length of names
len(names)


# ### Step 9. What is the name with most occurrences?

# In[151]:

names.Count.idxmax()

# OR

# names[names.Count == names.Count.max()]


# ### Step 10. How many different names have the least occurrences?

# In[138]:

len(names[names.Count == names.Count.min()])


# ### Step 11. What is the median name occurrence?

# In[144]:

names[names.Count == names.Count.median()]


# ### Step 12. What is the standard deviation of names?

# In[147]:

names.Count.std()


# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

# In[148]:

names.describe()

