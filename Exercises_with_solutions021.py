
# coding: utf-8

# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[3]:

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')


# ### Step 4. How many products cost more than $10.00?

# In[4]:

# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices 

# make the comparison
chipo10 = chipo[chipo['item_price'] > 10.00]
chipo10.head()

len(chipo10)


# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# In[9]:

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity'])

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]

# select only the item_name and item_price columns
price_per_item = chipo_one_prod[['item_name', 'item_price']]

# sort the values from the most to less expensive
price_per_item.sort_values(by = "item_price", ascending = False)


# ### Step 6. Sort by the name of the item

# In[156]:

chipo.item_name.sort_values()

# OR

chipo.sort_values(by = "item_name")


# ### Step 7. What was the quantity of the most expensive item ordered?

# In[165]:

chipo.sort_values(by = "item_price", ascending = False).head(1)


# ### Step 8. How many times were a Veggie Salad Bowl ordered?

# In[174]:

chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)


# ### Step 9. How many times people orderd more than one Canned Soda?

# In[5]:

chipo_drink_steak_bowl = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
len(chipo_drink_steak_bowl)

