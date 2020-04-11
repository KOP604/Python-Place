
# coding: utf-8

# # Fictional Army - Filtering and Sorting

# ### Introduction:
# 
# This exercise was inspired by this [page](http://chrisalbon.com/python/)
# 
# Special thanks to: https://github.com/chrisalbon for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. This is the data given as a dictionary

# In[9]:

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}


# ### Step 3. Create a dataframe and assign it to a variable called army. 
# 
# #### Don't forget to include the columns names

# In[19]:

army = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'deaths', 'battles', 'size', 'veterans', 'readiness', 'armored', 'deserters', 'origin'])


# ### Step 4. Set the 'origin' colum as the index of the dataframe

# In[20]:

army = army.set_index('origin')
army


# ### Step 5. Print only the column veterans

# In[12]:

army['veterans']


# ### Step 6. Print the columns 'veterans' and 'deaths'

# In[13]:

army[['veterans', 'deaths']]


# ### Step 7. Print the name of all the columns.

# In[16]:

army.columns


# ### Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska

# In[24]:

# Select all rows with the index label "Maine" and "Alaska"
army.loc[['Maine','Alaska'] , ["deaths","size","deserters"]]


# ### Step 9. Select the rows 3 to 7 and the columns 3 to 6

# In[26]:

#
army.iloc[3:7, 3:6]


# ### Step 10. Select every row after the fourth row

# In[28]:

army.iloc[3:]


# ### Step 11. Select every row up to the 4th row

# In[30]:

army.iloc[:3]


# ### Step 12. Select the 3rd column up to the 7th column

# In[32]:

# the first : means all
# after the comma you select the range

army.iloc[: , 4:7]


# ### Step 13. Select rows where df.deaths is greater than 50

# In[33]:

army[army['deaths'] > 50]


# ### Step 14. Select rows where df.deaths is greater than 500 or less than 50

# In[35]:

army[(army['deaths'] > 500) | (army['deaths'] < 50)]


# ### Step 15. Select all the regiments not named "Dragoons"

# In[37]:

army[(army['regiment'] != 'Dragoons')]


# ### Step 16. Select the rows called Texas and Arizona

# In[38]:

army.ix[['Arizona', 'Texas']]


# ### Step 17. Select the third cell in the row named Arizona

# In[41]:

army.ix['Arizona', 'deaths']

#OR

army.ix['Arizona', 2]


# ### Step 18. Select the third cell down in the column named deaths

# In[43]:

army.ix[2, 'deaths']

