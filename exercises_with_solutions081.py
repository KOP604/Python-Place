
# coding: utf-8

# # Pokemon

# ### Introduction:
# 
# This time you will create the data.
# 
# 
# 
# ### Step 1. Import the necessary libraries

# In[2]:

import pandas as pd


# ### Step 2. Create a data dictionary

# In[3]:

raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }


# ### Step 3. Assign it to a variable called 

# In[5]:

pokemon = pd.DataFrame(raw_data)
pokemon.head()


# ### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex

# In[8]:

pokemon = pokemon[['name', 'type', 'hp', 'evolution','pokedex']]
pokemon


# ### Step 5. Add another column called place, and insert what you have in mind.

# In[13]:

pokemon['place'] = ['park','street','lake','forest']
pokemon


# ### Step 6. Present the type of each column

# In[9]:

pokemon.dtypes


# ### BONUS: Create your own question and answer it.

# In[ ]:



