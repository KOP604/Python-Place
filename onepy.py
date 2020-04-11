# coding: utf-8

# # Ex2 - Getting and Knowing your Data
# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries
# In[1]:

import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address]
#(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 
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
chipo.shape[0]  # 0 represents row


# In[5]:

# Solution 2
chipo.info() # entries <= 4622 observations


# ### Step 6. What is the number of columns in the dataset?

# In[6]:

chipo.shape[1] #1 represents column



# ### Step 7. Print the name of all the columns.

# In[7]:

chipo.columns

# ### Step 8. How is the dataset indexed?

# In[8]:

chipo.index


# ### Step 9. Which was the most-ordered item? 

#### In[9]:
    
chipo.groupby('item_name').sum().sort_values(['quantity'],ascending=False).head(1)
chipo.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(1)


#both qorked
c = chipo.groupby('item_name')  # GROUPBY object that rearranges data by group id itself is DF
c.size() # # rows by group

# for example we see c id very different from chipo
len(chipo)  #4622
len(c)      # 50
chipo['item_name'].nunique() #50

chipo['item_name'].value_counts()
     
c['quantity'].sum().sort_values(ascending=False).head(1)


    


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


# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[2]:

users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')


# ### Step 4. See the first 25 entries

# In[3]:

users.head(25)


# ### Step 5. See the last 10 entries

# In[4]:

users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[5]:

users.shape[0]


# ### Step 7. What is the number of columns in the dataset?

# In[6]:

users.shape[1]


# ### Step 8. Print the name of all the columns.

# In[7]:

users.columns


# ### Step 9. How is the dataset indexed?

# In[8]:

# "the index" (aka "the labels")
users.index


# ### Step 10. What is the data type of each column?

# In[9]:

users.dtypes


# ### Step 11. Print only the occupation column

# In[10]:

users.occupation 

#OR

users['occupation']


# ### Step 12. How many different occupations there are in this dataset?

# In[14]:

users.occupation.nunique()


# ### Step 13. What is the most frequent occupation?

# In[15]:

users.occupation.value_counts().head()


# ### Step 14. Summarize the DataFrame.

# In[16]:

users.describe() #Notice is only the numeric column


# ### Step 15. Summarize all the columns

# In[17]:

users.describe(include = "all") #Notice is only the numeric column


# ### Step 16. Summarize only the occupation column

# In[18]:

users.occupation.describe()


# ### Step 17. What is the mean age of users?

# In[19]:

round(users.age.mean())


# ### Step 18. What is the age with least occurrence?

# In[20]:

users.age.value_counts().tail(1) #7 years, only 1 occurrence


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


# coding: utf-8

# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarizes as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 

# ### Step 3. Assign it to a variable called drinks.

# In[4]:

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()


# ### Step 4. Which continent drinks more beer on average?

# In[6]:

drinks.groupby('continent').beer_servings.mean()


# ### Step 5. For each continent print the statistics for wine consumption.

# In[9]:

drinks.groupby('continent').wine_servings.describe()


# ### Step 6. Print the mean alcoohol consumption per continent for every column

# In[10]:

drinks.groupby('continent').mean()


# ### Step 7. Print the median alcoohol consumption per continent for every column

# In[14]:

drinks.groupby('continent').median()


# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# In[15]:

drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])


# coding: utf-8

# # Occupation

# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[64]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users.

# In[65]:

users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')
users.head()


# ### Step 4. Discover what is the mean age per occupation

# In[66]:

users.groupby('occupation').age.mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[150]:

# create a function
def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)


a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100 

# sort to the most male 
a.sort_values(ascending = False)


# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[151]:

users.groupby('occupation').age.agg(['min', 'max'])


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[152]:

users.groupby(['occupation', 'gender']).age.mean()


# ### Step 8.  For each occupation present the percentage of women and men

# In[154]:

# create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

# present all rows from the 'gender column'
occup_gender.loc[: , 'gender']


# coding: utf-8

# # Regiment

# ### Introduction:
# 
# Special thanks to: http://chrisalbon.com/ for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Create the DataFrame with the following values:

# In[4]:

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}


# ### Step 3. Assign it to a variable called regiment.
# #### Don't forget to name each column

# In[6]:

regiment = pd.DataFrame(raw_data, columns = raw_data.keys())
regiment


# ### Step 4. What is the mean preTestScore from the regiment Nighthawks?  

# In[26]:

regiment[regiment['regiment'] == 'Nighthawks'].groupby('regiment').mean()


# ### Step 5. Present general statistics by company

# In[29]:

regiment.groupby('company').describe()


# ### Step 6. What is the mean each company's preTestScore?

# In[33]:

regiment.groupby('company').preTestScore.mean()


# ### Step 7. Present the mean preTestScores grouped by regiment and company

# In[35]:

regiment.groupby(['regiment', 'company']).preTestScore.mean()


# ### Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing

# In[36]:

regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack()


# ### Step 9. Group the entire dataframe by regiment and company

# In[37]:

regiment.groupby(['regiment', 'company']).mean()


# ### Step 10. What is the number of observations in each regiment and company

# In[41]:

regiment.groupby(['company', 'regiment']).size()


# ### Step 11. Iterate over a group and print the name and the whole data from the regiment

# In[50]:

# Group the dataframe by regiment, and for each regiment,
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)


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


# coding: utf-8

# # United States - Crime Rates - 1960 - 2014

# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[95]:

import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 

# ### Step 3. Assign it to a variable called crime.

# In[265]:

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()


# ### Step 4. What is the type of the columns?

# In[266]:

crime.info()


# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

# In[267]:

# pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()


# ### Step 6. Set the Year column as the index of the dataframe

# In[268]:

crime = crime.set_index('Year', drop = True)
crime.head()


# ### Step 7. Delete the Total column

# In[269]:

del crime['Total']
crime.head()


# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

# In[270]:

# To learn more about .resample (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)
# To learn more about Offset Aliases (http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases)

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

crimes


# ### Step 9. What is the mos dangerous decade to live in the US?

# In[276]:

# apparently the 90s was a pretty dangerous time in the US
crime.idxmax(0)


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


# coding: utf-8

# # Fictitious Names

# ### Introduction:
# 
# This time you will create a data again 
# 
# Special thanks to [Chris Albon](http://chrisalbon.com/) for sharing the dataset and materials.
# All the credits to this exercise belongs to him.  
# 
# In order to understand about it go to [here](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/).
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd


# ### Step 2. Create the 3 DataFrames based on the followin raw data

# In[2]:

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}


# ### Step 3. Assign each to a variable called data1, data2, data3

# In[12]:

data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

data3


# ### Step 4. Join the two dataframes along rows and assign all_data

# In[9]:

all_data = pd.concat([data1, data2])
all_data


# ### Step 5. Join the two dataframes along columns and assing to all_data_col

# In[10]:

all_data_col = pd.concat([data1, data2], axis = 1)
all_data_col


# ### Step 6. Print data3

# In[13]:

data3


# ### Step 7. Merge all_data and data3 along the subject_id value

# In[15]:

pd.merge(all_data, data3, on='subject_id')


# ### Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2

# In[16]:

pd.merge(data1, data2, on='subject_id', how='inner')


# ### Step 9. Merge all values in data1 and data2, with matching records from both sides where available.

# In[17]:

pd.merge(data1, data2, on='subject_id', how='outer')


# coding: utf-8

# # Housing Market

# ### Introduction:
# 
# This time we will create our own dataset with fictional numbers to describe a house market. As we are going to create random data don't try to reason of the numbers.
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd
import numpy as np


# ### Step 2. Create 3 differents Series, each of length 100, as follows: 
# 1. The first a random number from 1 to 4 
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000

# In[28]:

s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

print s1, s2, s3


# ### Step 3. Let's create a DataFrame by joinning the Series by column

# In[29]:

housemkt = pd.concat([s1, s2, s3], axis=1)
housemkt.head()


# ### Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

# In[36]:

housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
housemkt.head()


# ### Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

# In[59]:

# join concat the values
bigcolumn = pd.concat([s1, s2, s3], axis=0)

# it is still a Series, so we need to transform it to a DataFrame
bigcolumn = bigcolumn.to_frame()
print type(bigcolumn)

bigcolumn


# ### Step 6. Ops it seems it is going only until index 99. Is it true?

# In[45]:

# no the index are kept but the length of the DataFrame is 300
len(bigcolumn)


# ### Step 7. Reindex the DataFrame so it goes from 0 to 299

# In[69]:

bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn


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


# coding: utf-8

# # Wind Statistics

# ### Introduction:
# 
# The data have been modified to contain some missing values, identified by NaN.  
# Using pandas should make this exercise
# easier, in particular for the bonus question.
# 
# You should be able to perform all of these operations without using
# a for loop or other looping construct.
# 
# 
# 1. The data in 'wind.data' has the following format:

# In[1]:

"""
Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
61  1  1 15.04 14.96 13.17  9.29   NaN  9.87 13.67 10.25 10.83 12.58 18.50 15.04
61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
"""


#    The first three columns are year, month and day.  The
#    remaining 12 columns are average windspeeds in knots at 12
#    locations in Ireland on that day.   
# 
#    More information about the dataset go [here](wind.desc).

# ### Step 1. Import the necessary libraries

# In[2]:

import pandas as pd
import datetime


# ### Step 2. Import the dataset from this [address](https://github.com/guipsamora/pandas_exercises/blob/master/Stats/Wind_Stats/wind.data)

# ### Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

# In[414]:

# parse_dates gets 0, 1, 2 columns and parses them as the index
data = pd.read_table("wind.data", sep = "\s+", parse_dates = [[0,1,2]]) 
data.head()


# ### Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.

# In[415]:

# The problem is that the dates are 2061 and so on...

# function that uses datetime
def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# data.info()
data.head()


# ### Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

# In[1]:

# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])

# set 'Yr_Mo_Dy' as the index
data = data.set_index('Yr_Mo_Dy')

data.head()
# data.info()


# ### Step 6. Compute how many values are missing for each location over the entire record.  
# #### They should be ignored in all calculations below. 

# In[423]:

# "Number of non-missing values for each location: "
data.isnull().sum()


# ### Step 7. Compute how many non-missing values there are in total.

# In[424]:

# number of columns minus the number of missing values for each location
data.shape[1] - data.isnull().sum()


# ### Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
# #### A single number for the entire dataset.

# In[426]:

# print 'Mean over all values is: '
data.mean().mean()


# ### Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days 
# 
# #### A different set of numbers for each location.

# In[264]:

loc_stats = pd.DataFrame()

loc_stats['min'] = data.min() # min
loc_stats['max'] = data.max() # max 
loc_stats['mean'] = data.mean() # mean
loc_stats['std'] = data.std() # standard deviations

loc_stats


# ### Step 10. Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day.
# 
# #### A different set of numbers for each day.

# In[404]:

# create the dataframe
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max 
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

day_stats.head()


# ### Step 11. Find the average windspeed in January for each location.  
# #### Treat January 1961 and January 1962 both as January.

# In[427]:

# print "January windspeeds:"

# creates a new column 'date' and gets the values from the index
data['date'] = data.index

# creates a column for each value from date
data['month'] = data['date'].apply(lambda date: date.month)
data['year'] = data['date'].apply(lambda date: date.year)
data['day'] = data['date'].apply(lambda date: date.day)

# gets all value from the month 1 and assign to janyary_winds
january_winds = data.query('month == 1')

# gets the mean from january_winds, using .loc to not print the mean of month, year and day
january_winds.loc[:,'RPT':"MAL"].mean()


# ### Step 12. Downsample the record to a yearly frequency for each location.

# In[428]:

data.query('month == 1 and day == 1')


# ### Step 13. Downsample the record to a monthly frequency for each location.

# In[429]:

data.query('day == 1')


# ### Step 14. Downsample the record to a weekly frequency for each location.

# In[430]:

data[::7].head()


# ### Step 15. Calculate the mean windspeed for each month in the dataset.  
# #### Treat January 1961 and January 1962 as *different* months.
# #### (hint: first find a  way to create an identifier unique for each month.)

# In[3]:

# call data again but this time don't use parse_dates
wind_data = pd.read_table("wind.data", sep = "\s+") 

# compute the month number for each day in the dataset, there are in total 216 months
wind_data['months_num'] = (wind_data.iloc[:, 0] - 61) * 12 + wind_data.iloc[:, 1]

wind_data

# group the data according to the months_num and get the mean
# monthly_data = wind_data.groupby(['months_num']).mean()

# monthly_data.head()


# ### Step 16. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

# In[433]:

# resample data to 'W' week and use the functions
weekly = data.resample('W').agg(['min','max','mean','std'])

# slice it for the first 52 weeks and locations
weekly.ix[1:53, "RPT":"MAL"].head(10)


# coding: utf-8

# # Visualizing Chipotle's Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[132]:

import pandas as pd
import collections
import matplotlib.pyplot as plt 

# set this so the 
get_ipython().magic('matplotlib inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[133]:

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')


# ### Step 4. See the first 10 entries

# In[134]:

chipo.head(10)


# ### Step 5. Create a histogram of the top 5 items bought

# In[135]:

# get the Series of the names
x = chipo.item_name

# use the Counter class from collections to create a dictionary with keys(text) and frequency
letter_counts = Counter(x)

# convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(letter_counts, orient='index')

# sort the values from the top to the least value and slice the first 5 items
df = df[0].sort_values(ascending = True)[45:50]

# create the plot
df.plot(kind='bar')

# Set the title and labels
plt.xlabel('Items')
plt.ylabel('Price')
plt.title('Most ordered Chipotle\'s Items')

# show the plot
plt.show()


# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis

# In[136]:

# create a list of prices
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space

# then groupby the orders and sum
orders = chipo.groupby('order_id').sum()

# creates the scatterplot
# plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')

# Set the title and labels
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
plt.ylim(0)


# ### BONUS: Create a question and a graph to answer your own question.

# In[ ]:




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




# coding: utf-8

# # Scores

# ### Introduction:
# 
# This time you will create the data.
# 
# ***Exercise based on [Chris Albon](http://chrisalbon.com/) work, the credits belong to him.***
# 
# ### Step 1. Import the necessary libraries

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib inline')


# ### Step 2. Create the DataFrame it should look like below.

# In[2]:

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
            'female': [0, 1, 1, 0, 1],
            'age': [42, 52, 36, 24, 73], 
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

df


# ### Step 3. Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
# #### Hint: Don't forget to place the labels

# In[5]:

plt.scatter(df.preTestScore, df.postTestScore, s=df.age)

#set labels and titles
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')


# ### Step 4. Create a Scatterplot of preTestScore and postTestScore.
# ### This time the size should be 4.5 times the postTestScore and the color determined by sex

# In[10]:

plt.scatter(df.preTestScore, df.postTestScore, s= df.postTestScore * 4.5, c = df.female)

#set labels and titles
plt.title("preTestScore x postTestScore")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')


# ### BONUS: Create your own question and answer it.

# In[ ]:




# coding: utf-8

# # Visualizing the Titanic Disaster

# ### Introduction:
# 
# This exercise is based on the titanic Disaster dataset avaiable at [Kaggle](https://www.kaggle.com/c/titanic).  
# To know more about the variables check [here](https://www.kaggle.com/c/titanic/data)
# 
# 
# ### Step 1. Import the necessary libraries

# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

get_ipython().magic('matplotlib inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Titanic_Desaster/train.csv). 

# ### Step 3. Assign it to a variable titanic 

# In[4]:

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/Visualization/Titanic_Desaster/train.csv'

titanic = pd.read_csv(url)

titanic.head()


# ### Step 4. Set PassengerId as the index 

# In[5]:

titanic.set_index('PassengerId').head()


# ### Step 5. Create a pie chart presenting the male/female proportion

# In[24]:

# sum the instances of males and females
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()

# put them into a list called proportions
proportions = [males, females]

# Create a pie chart
plt.pie(
    # using proportions
    proportions,
    
    # with the labels being officer names
    labels = ['Males', 'Females'],
    
    # with no shadows
    shadow = False,
    
    # with colors
    colors = ['blue','red'],
    
    # with one slide exploded out
    explode = (0.15 , 0),
    
    # with the start angle at 90%
    startangle = 90,
    
    # with the percent listed as a fraction
    autopct = '%1.1f%%'
    )

# View the plot drop above
plt.axis('equal')

# Set labels
plt.title("Sex Proportion")

# View the plot
plt.tight_layout()
plt.show()


# ### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender

# In[67]:

# creates the plot using
lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)

# set title
lm.set(title = 'Fare x Age')

# get the axes object and tweak it
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)


# ### Step 7. How many people survived?

# In[68]:

titanic.Survived.sum()


# ### Step 8. Create a histogram with the Fare payed

# In[48]:

# sort the values from the top to the least value and slice the first 5 items
df = titanic.Fare.sort_values(ascending = False)
df

# create bins interval using numpy
binsVal = np.arange(0,600,10)
binsVal

# create the plot
plt.hist(df, bins = binsVal)

# Set the title and labels
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')

# show the plot
plt.show()


# ### BONUS: Create your own question and answer it.

# In[ ]:




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




# coding: utf-8

# # Apple Stock

# ### Introduction:
# 
# We are going to use Apple's stock price.
# 
# 
# ### Step 1. Import the necessary libraries

# In[4]:

import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)

# ### Step 3. Assign it to a variable apple

# In[32]:

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

apple.head()


# ### Step 4.  Check out the type of the columns

# In[33]:

apple.dtypes


# ### Step 5. Transform the Date column as a datetime type

# In[34]:

apple.Date = pd.to_datetime(apple.Date)

apple['Date'].head()


# ### Step 6.  Set the date as the index

# In[35]:

apple = apple.set_index('Date')

apple.head()


# ### Step 7.  Is there any duplicate dates?

# In[36]:

# NO! All are unique
apple.index.is_unique


# ### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.

# In[39]:

apple.sort_index(ascending = True).head()


# ### Step 9. Get the last business day of each month

# In[48]:

apple_month = apple.resample('BM').mean()

apple_month.head()


# ### Step 10.  What is the difference in days between the first day and the oldest

# In[65]:

(apple.index.max() - apple.index.min()).days


# ### Step 11.  How many months in the data we have?

# In[66]:

apple_months = apple.resample('BM').mean()

len(apple_months.index)


# ### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches

# In[81]:

# makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)


# ### BONUS: Create your own question and answer it.

# In[ ]:




# coding: utf-8

# # Getting Financial Data - Google Finance

# ### Introduction:
# 
# This time you will get data from a website.
# 
# 
# ### Step 1. Import the necessary libraries

# In[30]:

import pandas as pd

# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb

# package for dates
import datetime as dt


# ### Step 2. Create your time range (start and end variables). The start date should be 01/01/2015 and the end should today (whatever your today is)

# In[75]:

start = dt.datetime(2015, 1, 1)

end = dt.datetime.today()

start


# ### Step 3. Select the Apple, Tesla, Twitter, IBM, LinkedIn stocks symbols and assign them to a variable called stocks

# In[76]:

stocks = ['AAPL', 'TSLA', 'IBM', 'LNKD']


# ### Step 4. Read the data from google, assign to df and print it

# In[77]:

df = web.DataReader(stocks, 'google', start, end)
df


# ### Step 5.  What is the type of structure of df ?

# In[ ]:

# 'pandas.core.panel.Panel'


# ### Step 6. Print all the Items axis values
# #### To learn more about the Panel structure go to [documentation](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panel) 

# In[120]:

df.items


# ### Step 7. Good, now we know  the data avaiable. Create a dataFrame called vol, with the Volume values.

# In[122]:

vol = df['Volume']
vol.head()


# ### Step 8. Aggregate the data of Volume to weekly
# #### Hint: Be careful to not sum data from the same week of 2015 and other years.

# In[132]:

vol['week'] = vol.index.week
vol['year'] = vol.index.year

week = vol.groupby(['week','year']).sum()
week.head()


# ### Step 9. Find all the volume traded in the year of 2015

# In[131]:

del vol['week']
vol['year'] = vol.index.year

year = vol.groupby(['year']).sum()
year


# ### BONUS: Create your own question and answer it.

# In[ ]:




# coding: utf-8

# # Investor - Flow of Funds - US

# ### Introduction:
# 
# Special thanks to: https://github.com/rgrp for sharing the dataset.
# 
# ### Step 1. Import the necessary libraries

# In[30]:

import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv). 

# ### Step 3. Assign it to a variable called 

# In[31]:

url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
df = pd.read_csv(url)
df.head()


# ### Step 4.  What is the frequency of the dataset?

# In[32]:

# weekly data


# ### Step 5. Set the column Date as the index.

# In[33]:

df = df.set_index('Date')
df.head()


# ### Step 6. What is the type of the index?

# In[34]:

df.index
# it is a 'object' type


# ### Step 7. Set the index to a DatetimeIndex type

# In[35]:

df.index = pd.to_datetime(df.index)
type(df.index)


# ### Step 8.  Change the frequency to monthly, sum the values and assign it to monthly.

# In[36]:

monthly = df.resample('M').sum()
monthly


# ### Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.

# In[37]:

monthly = monthly.dropna()
monthly


# ### Step 10. Good, now we have the monthly data. Now change the frequency to year.

# In[38]:

year = monthly.resample('AS-JAN').sum()
year


# ### BONUS: Create your own question and answer it.

# In[ ]:



