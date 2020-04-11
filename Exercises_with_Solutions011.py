
# coding: utf-8

# # Ex2 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


print("Hello World")

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[2]:

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')


# ### Step 4. See the first 10 entries

# In[3]:

chipo.head(10)


# ### Step 5. What is the number of observations in the dataset?

# In[4]:

# Solution 1

chipo.shape[0]  # entries <= 4622 observations


# In[5]:

# Solution 2

chipo.info() # entries <= 4622 observations


# ### Step 6. What is the number of columns in the dataset?

# In[6]:

chipo.shape[1]


# ### Step 7. Print the name of all the columns.

# In[7]:

chipo.columns


# ### Step 8. How is the dataset indexed?

# In[8]:

chipo.index


# ### Step 9. Which was the most-ordered item? 

# In[9]:

c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)


# ### Step 10. For the most-ordered item, how many items were ordered?

# In[10]:

c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)


# ### Step 11. What was the most ordered item in the choice_description column?

# In[11]:

c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
c.head(1)
# Diet Coke 159


# ### Step 12. How many items were orderd in total?

# In[12]:

total_items_orders = chipo.quantity.sum()
total_items_orders


# ### Step 13. Turn the item price into a float

# #### Step 13.a. Check the item price type

# In[13]:

chipo.item_price.dtype


# #### Step 13.b. Create a lambda function and change the type of item price

# In[14]:

dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)


# #### Step 13.c. Check the item price type

# In[15]:

chipo.item_price.dtype


# ### Step 14. How much was the revenue for the period in the dataset?

# In[16]:

revenue = (chipo['quantity']* chipo['item_price']).sum()

print('Revenue was: $' + str(np.round(revenue,2)))


# ### Step 15. How many orders were made in the period?

# In[17]:

chipo.order_id.value_counts().count()


# ### Step 16. What is the average amount per order?

# In[18]:

# Solution 1

chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['item_price']


# In[19]:

# Solution 2

chipo.groupby(by=['order_id']).sum().mean()['item_price']


# ### Step 17. How many different items are sold?

# In[20]:

chipo.item_name.value_counts().count()

