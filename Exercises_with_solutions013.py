
# coding: utf-8

# # Ex1 - Getting and knowing your Data

# ### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data

# ###  Step 2. Download the dataset to your computer and unzip it.

# In[2]:

import pandas as pd
import numpy as np


# ### Step 3. Use the tsv file and assign it to a dataframe called food

# In[4]:

food = pd.read_csv('~/Desktop/en.openfoodfacts.org.products.tsv', sep='\t')


# ### Step 4. See the first 5 entries

# In[5]:

food.head()


# ### Step 5. What is the number of observations in the dataset?

# In[7]:

food.shape #will give you both (observations/rows, columns)


# In[8]:

food.shape[0] #will give you only the observations/rows number


# ### Step 6. What is the number of columns in the dataset?

# In[10]:

print(food.shape) #will give you both (observations/rows, columns)
print(food.shape[1]) #will give you only the columns number

#OR

food.info() #Columns: 159 entries


# ### Step 7. Print the name of all the columns.

# In[11]:

food.columns


# ### Step 8. What is the name of 105th column?

# In[12]:

food.columns[104]


# ### Step 9. What is the type of the observations of the 105th column?

# In[15]:

food.dtypes['-glucose_100g']


# ### Step 10. How is the dataset indexed?

# In[16]:

food.index


# ### Step 11. What is the product name of the 19th observation?

# In[17]:

food.values[18][7]

