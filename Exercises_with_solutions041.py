
# coding: utf-8

# # Student Alcohol Consumption

# ### Introduction:
# 
# This time you will download a dataset from the UCI.
# 
# ### Step 1. Import the necessary libraries

# In[24]:

import pandas as pd
import numpy


# ### Step 2. Import the dataset from this [address](https://github.com/guipsamora/pandas_exercises/blob/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).

# ### Step 3. Assign it to a variable called df.

# In[25]:

df = pd.read_csv('/Users/guilhermeoliveira/Desktop/student/student-mat.csv', sep = ';')
df.head()


# ### Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column

# In[26]:

stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()


# ### Step 5. Create a lambda function that captalize strings.

# In[27]:

captalizer = lambda x: x.upper()


# ### Step 6. Capitalize both Mjob and Fjob

# In[28]:

stud_alcoh['Mjob'].apply(captalizer)
stud_alcoh['Fjob'].apply(captalizer)


# ### Step 7. Print the last elements of the data set.

# In[29]:

stud_alcoh.tail()


# ### Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and captalize Mjob and Fjob.

# In[30]:

stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(captalizer)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(captalizer)
stud_alcoh.tail()


# ### Step 9. Create a function called majority that return a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)

# In[31]:

def majority(x):
    if x > 17:
        return True
    else:
        return False


# In[32]:

stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()


# ### Step 10. Multiply every number of the dataset by 10. 
# ##### I know this makes no sense, don't forget it is just an exercise

# In[40]:

def times10(x):
    if type(x) is int:
        return 10 * x
    return x


# In[42]:

stud_alcoh.applymap(times10).head(10)

