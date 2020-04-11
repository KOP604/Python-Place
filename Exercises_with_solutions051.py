
# coding: utf-8

# # MPG Cars

# ### Introduction:
# 
# The following exercise utilizes data from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
# 
# ### Step 1. Import the necessary libraries

# In[24]:

import pandas as pd
import numpy as np


# ### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv).  

#    ### Step 3. Assign each to a to a variable called cars1 and cars2

# In[2]:

cars1 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
cars2 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")

print cars1.head()
print cars2.head()


# ### Step 4. Ops it seems our first dataset has some unnamed blank columns, fix cars1

# In[12]:

cars1 = cars1.loc[:, "mpg":"car"]
cars1.head()


# ### Step 5. What is the number of observations in each dataset?

# In[14]:

print cars1.shape
print cars2.shape


# ### Step 6. Join cars1 and cars2 into a single DataFrame called cars

# In[23]:

cars = cars1.append(cars2)
cars


# ### Step 7. Ops there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.

# In[33]:

nr_owners = np.random.randint(15000, high=73001, size=398, dtype='l')
nr_owners


# ### Step 8. Add the column owners to cars

# In[34]:

cars['owners'] = nr_owners
cars.tail()

