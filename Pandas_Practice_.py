
# coding: utf-8

# In[2]:

#. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
K=[1,2,3,4,5,6,7,8,99,4823]
Kd=pd.Series(K)


# In[5]:

type(Kd)


# In[6]:

Kd.head()


# In[9]:

#3.. Write a Python program to add, subtract, multiple and divide two Pandas Series. 
Kd2=pd.Series([98,23,10,65,1099,6,24,856,9,10])
#Kd+Kd2
#Kd-Kd2
Kd2/Kd


# In[4]:

#4 Write a Python program to get the largest integer smaller or equal to the division of the inputs.
ecom=pd.read_csv("D://Python/Ecommerce+Purchases-Copy1.csv")


# ### Python Pandas DataFrame [22 exercises with solution]

# In[5]:

#1. Write a Python program to get the powers of an array values element-wise. 
#Note: First array elements raised to powers from second array
#Original array 
#[0 1 2 3 4 5 6] 
#First array elements raised to powers from second array, element-wise: 
#[ 0 1 8 27 64 125 216]
def power3(x):
    return x**3

par=pd.Series([0,1,2,3,4,5,6])
par.apply(power3)
    


# In[56]:

#2 Write a Python program to create and display a DataFrame from a specified dictionary data which has the index labels.
import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_df=pd.DataFrame(exam_data, index=labels) #注意如何构造LABELS
exam_df


# In[11]:

#3. Write a Python program to display a summary of the basic information about a specified DataFrame and its data.
exam_df.info()


# In[12]:

#4. Write a Python program to get the first 3 rows of a given DataFrame
exam_df.head(3)


# In[34]:

#5. Write a Python program to select the 'name' and 'score' columns from the following 
exam_df[['name','score']]


# In[27]:

#6. Write a Python program to select the specified columns and rows from a given data frame. Go to the editor
#Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
exam_df.loc[[0,2,4,5], ['name','score']]


# In[36]:

#7. Write a Python program to select the rows where the number of attempts in the examination is greater than 2. 
sc=exam_df["attempts"]>2
exam_df[sc]


# In[37]:

#8. Write a Python program to count the number of rows and columns of a DataFrame
exam_df.shape


# In[4]:

#9. Write a Python program to select the rows where the score is missing, i.e. is NaN
exam_df[exam_df['score'].isnull()]


# In[165]:

#10. Write a Python program to select the rows the score is between 15 and 20 (inclusive). 
#exam_df[(exam_df["score"]>=15) & (exam_df["score"]<=20)] #OK
#exam_df.loc[(exam_df["score"]>=15) & (exam_df["score"]<=20)] #OK
exam_df.loc[(exam_df["score"]>=15) & (exam_df["score"]<=20),:] #OK


# In[7]:

#11. Write a Python program to select the rows where number of attempts in the examination
#is less than 2 and score greater than 15. Go to the edito
#dc=(exam_df["score"]>=15) & (exam_df["attempts"]<=2)

exam_df[(exam_df["score"]>=15) & (exam_df["score"]<=20)]

#exam_df.loc[(exam_df["score"]>=15) & (exam_df["score"]<=20)]


# In[26]:

#12. Write a Python program to change the score in row 'd' to 11.5. Go to the editor
#exam_df.iloc[3,1]=11.5
exam_df.loc[3,'score']=13.5
        


# In[104]:

#alternatively
df3.iloc[3]['score']=24 #not good
#df3.loc['d']['score']


# In[27]:

#13. Write a Python program to calculate the sum of the examination attempts by the students.
exam_df['attempts'].sum()


# In[64]:

#14Write a Python program to calculate the mean score for each different student in DataFrame. Go to the editor
exam_df['mean_score']=exam_df['score']/exam_df['attempts']
exam_df


# In[55]:

exam_df


# In[68]:

#15. Write a Python program to append a new row 'k' to data frame with given values for each column. 
#Now delete the new row and return the original DataFrame. 

# 下面三种方法都可以

#1. 不行
#df3=exam_df.copy()
#df3.append(['Peter',18, 2,'yes'])
#df3

#2.
df3=exam_df.copy()
#df3.loc['k']=['Peter',18, 2,'yes']
#df3
df3.loc['k']={'name': ['Peter'],'score':[18],'attempts':[2],'qualify':['yes']} #这个也可以
df3

#3. 不行
#df3=exam_df.copy()
#df2 = pd.Series(['Peter',18, 2,'yes'])  
#df3.append(df2, ignore_index=True)
#df3

#df3.drop('k')
    


# In[70]:

#16. Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. Go 
df3=exam_df
#df3.sort_values(by='name',ascending=False)
df3.sort_values(by='score',ascending=True)


# In[74]:

#17. Write a Python program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. Go to the editor
#df3=exam_df.copy()
df3['qualify'].replace(['yes','no'],[True, False])


# In[75]:

#18. Write a Python program to change the name 'James' to 'Suresh' in name column of the DataFrame. Go to the edit
df3=exam_df.copy()
df3['name'].replace('James','Suresh')


# In[78]:

#19. Write a Python program to delete the 'attempts' column from the DataFram
df3=exam_df.copy()
df3.drop('attempts',axis=1)


# In[81]:

#20. Write a Python program to insert a new column in existing DataFrame. 
df3=exam_df.copy()
#df3['new_col']=df3['score']**2
df3['new_col']=''
df3


# In[83]:

#21Write a Python program to iterate over rows in a DataFrame
#see next cell


# In[154]:

df3=exam_df.copy()
#df3.loc[['h','j'], ['name','score']] OK
#df3.iloc[1:5,[0,1,3]]  OK
#df3.loc[df3.index[3:5], ['name','score']]  OK
#df3.iloc[2:4]['name'] OK
#df3.iloc[2:4, 2:4] OK
#df3.loc[:, ['name','score']] OK
#df3.loc[df3['name']=='Dima', 'score'] OK




# In[158]:

#alternative to 21
df3=exam_df.copy()
for i in range(0, len(df3)):
    #print(df3.iloc[i]['name'], df3.iloc[i]['score']) #这样做的好处是两个变量输出在一行
    print(df3.iloc[i, 0:2]) #这样就是两行    


# In[113]:

for i in range(0, len(df3)):
    df3.loc[i,'score']=3456
df3 #bit right


# In[160]:

#22. Write a Python program to get list from DataFrame column headers. Go to the editor
df3=exam_df.copy()
#eithetr way
list(df3.columns.values)


# ### END
