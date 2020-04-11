
# coding: utf-8

# # Online Retails Purchase

# ### Introduction:
# 
# 
# 
# ### Step 1. Import the necessary libraries

# In[197]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set the graphs to show in the jupyter notebook
get_ipython().magic('matplotlib inline')

# set seabor graphs to a better style
sns.set(style="ticks")


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Online_Retail/Online_Retail.csv). 

# ### Step 3. Assign it to a variable called online_rt

# In[198]:

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Online_Retail/Online_Retail.csv'
online_rt = pd.read_csv(url)

online_rt.head()


# ### Step 4. Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK

# In[199]:

# group by the Country
countries = online_rt.groupby('Country').sum()

# sort the value and get the first 10 after UK
countries = countries.sort_values(by = 'Quantity',ascending = False)[1:11]

# create the plot
countries['Quantity'].plot(kind='bar')

# Set the title and labels
plt.xlabel('Countries')
plt.ylabel('Quantity')
plt.title('10 Countries with more orders')

# show the plot
plt.show()


# ### Step 5.  Exclude negative Quatity entries

# In[200]:

online_rt = online_rt[online_rt.Quantity > 0]
online_rt.head()


# ### Step 6. Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries

# In[201]:

# groupby CustomerID
customers = online_rt.groupby(['CustomerID','Country']).sum()

# there is an outlier with negative price
customers = customers[customers.UnitPrice > 0]

# get the value of the index and put in the column Country
customers['Country'] = customers.index.get_level_values(1)

# top three countries
top_countries =  ['Netherlands', 'EIRE', 'Germany']

# filter the dataframe to just select ones in the top_countries
customers = customers[customers['Country'].isin(top_countries)]

################
# Grap Section #
################

# creates the FaceGrid
g = sns.FacetGrid(customers, col="Country")

# map over a make a scatterplot
g.map(plt.scatter, "Quantity", "UnitPrice", alpha=1)

# adds legend
g.add_legend();


# ### BONUS: Create your own question and answer it.

# In[ ]:



