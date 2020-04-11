
# coding: utf-8

# # Ex2 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# In[25]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/jokecamp/FootballData/master/UEFA_European_Championship/Euro%202012/Euro%202012%20stats%20TEAM.csv). 

# ### Step 3. Assign it to a variable called euro12.

# In[36]:

euro12 = pd.read_csv('https://raw.githubusercontent.com/jokecamp/FootballData/master/UEFA_European_Championship/Euro%202012/Euro%202012%20stats%20TEAM.csv', sep=',')
euro12


# ### Step 4. Select only the Goal column.

# In[37]:

euro12.Goals


# ### Step 5. How many team participated in the Euro2012?

# In[43]:

euro12.shape[0]


# ### Step 6. What is the number of columns in the dataset?

# In[44]:

euro12.info()


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[82]:

# filter only giving the column names

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[56]:

discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[55]:

round(discipline['Yellow Cards'].mean())


# ### Step 10. Filter teams that scored more than 6 goals

# In[57]:

euro12[euro12.Goals > 6]


# ### Step 11. Select the teams that start with G

# In[66]:

euro12[euro12.Team.str.startswith('G')]


# ### Step 12. Select the first 7 columns

# In[84]:

# use .iloc to slices via the position of the passed integers
# : means all, 0:7 means from 0 to 7

euro.iloc[: , 0:7]


# ### Step 13. Select all columns except the last 3.

# In[86]:

# use negative to exclude the last 3 columns

euro.iloc[: , :-3]


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[89]:

# .loc is another way to slice, using the labels of the columns and indexes

euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]

