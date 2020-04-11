
# coding: utf-8

# ### https://www.w3resource.com/python-exercises/pandas/index-dataframe.php 共63道题

# In[3]:

#. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

import pandas as pd
import numpy as np

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

#def power3(x):
#    return x**3

par=pd.Series([0,1,2,3,4,5,6])
par**3   


# In[6]:

#2 Write a Python program to create and display a DataFrame from a specified dictionary data which has the index labels.

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


# In[44]:

#5. Write a Python program to select the 'name' and 'score' columns from the following 

#exam_df['name']  #select column
#exam_df.loc['h'] #select row
#exam_df[0:3]
#exam_df[['name','qualify']]
#exam_df.iloc[1:3,2:3]
#exam_df[1:3]['attempts']
#exam_df.loc[:,['name','qualify']]
#exam_df.loc[['b','c'],['name','qualify']]
exam_df.iloc[2:7][['name','qualify']] #OK


# In[47]:

#6. Write a Python program to select the specified columns and rows from a given data frame. Go to the editor
#Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
#exam_df.iloc[[0,2,4,5], 2:3]
exam_df.iloc[0:4]['name']




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


# In[22]:

for i in range(0, len(df3)):
    df3.loc[i,'score']=3456
df3 #bit right


# In[160]:

#22. Write a Python program to get list from DataFrame column headers. Go to the editor
df3=exam_df.copy()
#eithetr way
list(df3.columns.values)


# In[4]:

# added execises 

df3=exam_df.copy()


# In[8]:

df3.groupby(by='qualify')['score'].mean()


# In[15]:

df3.groupby(by='qualify')['name'].count()


# In[17]:

df3['new']=0 #have to declare it first
df3.loc[(df3['qualify']=='no'), ['new']]=25
df3.loc[(df3['qualify']=='yes'), ['new']]=19


# In[23]:

df3.sort_values(by=['new','score'],ascending=[True, False] )


# In[50]:

df3=exam_df.copy()
d3_1=df3.loc[df3['qualify']=='no']
d3_2=df3.loc[df3['qualify']=='yes']


# In[82]:

Yate=exam_df.copy()
KJ=d3_1.append([d3_2]) #需要建立一个新的数据 否则append结果不能保存
d3_1.append(d3_2)
len(d3_1)


# In[117]:

Yate=exam_df.copy()
KJ=d3_1.append([d3_2]) 
KJ2=KJ.append(KJ)


# len(KJ2)

# In[118]:

#KJ2.columns
KJ2.info()


# In[119]:

import random
KJ2['new']=0 #不要用KJ2.loc 不然会加上一行
KJ2['new']=random.randint(1,101) #同样
KJ2


# In[144]:

#KJ2=exam_df.copy()
#KJ2['new']=0
#KJ2
#len(KJ2)
KJ2[3,'new']=12

#for i in range(0,len(KJ2)):
#    KJ2.iloc[i]['new']=random.randint(1,101) 


# KJ2

# In[145]:

KJ2


# In[126]:

import random
for x in range(10):
    print (random.randint(1,21)*5)


# In[3]:

#
df=pd.DataFrame({'key':['b','b','a','c','a','b'], 'data1': range(6)})
df


# In[5]:

pd.get_dummies(df['key'])


# In[6]:

dummies=pd.get_dummies(df['key'],prefix='key')


# In[8]:

df_with_dummy=df[['data1']].join(dummies)
df_with_dummy


# In[11]:

#32
Mydat=pd.DataFrame({'attempts':[1,3,2,3,2,3,1,1,2,1],
                    'name': ['Anastasia','Dima','Katherine','James','Emily','Michae','Matthew','Laura','Kevin','Jonas'],
                   'score':[12.5, 9.0,16.5, np.NaN, 9.0,20.0,14.5, np.NaN, 8.0,19.0],
                   'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']})
                            
Mydat2=Mydat.copy()
Mydat2['nscore']=Mydat['score'].replace(np.nan,0)
Mydat2.drop('score', axis=1)


# In[22]:

#35 Write a Pandas program to count the NaN values in one or more columns in DataFrame.
Mydat.isnull().sum() #随手做来 并无根据 可行


# In[23]:

#36Write a Pandas program to drop a list of rows from a specified DataFrame 2nd & 4th rows:
Mydat3=Mydat.drop([1,3], axis=0)


# In[24]:

Mydat3


# In[26]:

#37 reset the index for Mydat3
Mydat3.reset_index()


# In[40]:

#38  Write a Pandas program to devide a DataFrame in a given ratio. 70% and then 30%
K=np.random.randint(0,100, size=10)
Mydat2=Mydat.copy()
Mydat2['OD']=K



# In[45]:

Mydat3=Mydat2.sort_values(by='OD')
Mydat3.reset_index()
Mydat4=Mydat3[0:6]
Mydat4


# In[64]:

#39 combine series to form a dataframe
D1=pd.DataFrame({'D1': [100,200,'python',300.12,400]})
#D2=pd.DataFrame({'D2': [10,20,'php', 30.12,40]})
D2=pd.DataFrame({'D2': [10,20,3002, 30.12,40]})
D3=D1.merge(D2,left_index=True, right_index=True)


# In[65]:

D3


# In[68]:

#40. Write a Pandas program to shuffle a given DataFrame
Mydat3=Mydat.copy()
Mydat3['OD']=np.random.randint(0,1000, size=len(Mydat))
Mydat4=Mydat3.sort_values(by='OD')
Mydat4


# In[72]:

#41 Write a Pandas program to convert DataFrame column type from string to datetime.
DT=pd.DataFrame({'SD': ['3/11/2000', '3/12/2000', '3/13/2000']})
DT['TD']=pd.to_datetime(DT['SD'])
DT


# In[79]:

#42. Write a Pandas program to rename a specific column name in a given DataFrame
DT.rename(columns={"SD": "String"})


# In[87]:

#43 Write a Pandas program to get a list of a specified column of a DataFrame
ML=list(Mydat['score']) #瞎蒙就有
ML


# In[111]:

#44. Write a Pandas program to create a DataFrame from a Numpy array and specify the index column and column headers
#Index1 0 0.0 0.0
#Index2 0 0.0 0.0
#Index3 0 0.0 0.0
#.........
#Index12 0 0.0 0.0
#Index13 0 0.0 0.0
#Index14 0 0.0 0.0
#Index15 0 0.0 0.0

#X=np.array([0,0], [0,0])
x = np.array([[2,3,1,0],[2,3,1,0],[2,3,1,0],[2,3,1,0],[2,3,1,0],[2,3,1,0],[2,3,1,0]]) #注意双廓
dx=pd.DataFrame(x, columns=(['A','B','C','D']), index=([0,1,2,3,4,5,6,]))
dx


# In[114]:

#我自己的
df3 = pd.DataFrame(np.random.randn(10, 5), columns=(['A','B','C','D','E']), index=([0,1,2,3,4,5,6,7,8,9]))
df3


# In[119]:

#45. Write a Pandas program to find the row for where the value of a given column is maximum
ME=Mydat['score'].max()
Mydat[Mydat['score']==ME]


# In[136]:

#46. Write a Pandas program to check whether a given column is present in a DataFrame or not. Go to the editor
nlist=Mydat.columns
cnt=0
for i in range(0, len(nlist)):
    if nlist[cnt]=='name':
        print("Yes")
        break
    cnt+=1    
    
        


# In[143]:

#47. Write a Pandas program to get the specified row value of a given DataFrame
Mydat[4:5]


# In[145]:

#48. Write a Pandas program to get the datatypes of columns of a DataFrame
Mydat.dtypes #attribute not method


# In[146]:

#49 Write a Pandas program to append data to an empty DataFrame.
Ydat=pd.DataFrame()
Ydat.append(Mydat)


# In[152]:

#50. Write a Pandas program to sort a given DataFrame by two or more column
Mydat.sort_values(by=['attempts','name'], inplace=True, ascending=(False, False))


# In[153]:

Mydat


# In[154]:

#51 Write a Pandas program to convert the datatype of a given column (floats to ints).
Mydat.columns


# In[155]:

Mydat.dtypes


# In[157]:

Mydat['attempts'].astype(float)


# In[160]:

#52. Write a Pandas program to remove infinite values from a given DataFrame. 

MyS=pd.DataFrame({'SS':[1000.000000, 2000.000000, 3000.000000, -4000.000000, np.inf,-np.inf]})


# In[177]:

K=np.isfinite(MyS)
MyS2=MyS[K] #先转换成NaN 再DROPNA
MyS2.dropna()


# In[179]:

#53. Write a Pandas program to insert a given column at a specific column index in a DataFrame. Go to the editor
Mydat['addMe']=range(0,len(Mydat))


# In[183]:

Mydat.columns.values
Mydat[['addMe','attempts', 'name', 'score', 'qualify']]


# In[185]:

#54. Write a Pandas program to convert a given list of lists into a Dataframe.
Sdata=[[2, 4], [1, 3]]
Sdf=pd.DataFrame(Sdata)
Sdf
#0 2 4
#1 1 3


# In[207]:

#55. Write a Pandas program to group by the first column and get second column as lists in rows.
#Mydat.head()
#KM=Mydat.groupby('attempts')
#Mydat.columns.values
#Mydat.groupby('attempts')['score'].mean()

df = Mydat.groupby('attempts')['name'].apply(list) #LIST 很怪的用法
print("\nGroup on the attempts:")
print(df)


# In[217]:

#56. Write a Pandas program to get column index from column name of a given DataFrame. 
Mydat.columns.get_loc("score")


# In[218]:

#57. Write a Pandas program to count number of columns of a DataFrame
len(Mydat.columns)


# In[219]:

#58. Write a Pandas program to select all columns, except one given column in a DataFrame. Go to the editor
Mydat.iloc[:,[2,3,4,0]]


# In[220]:

#59. Write a Pandas program to get first n records of a DataFrame. 
Mydat.iloc[0:4,:]


# In[223]:

#60. Write a Pandas program to get last n records of a DataFrame
Mydat.iloc[-3:-1,:]


# In[224]:

#61. Write a Pandas program to get top most n records within each group of a DataFrame
Mydat.groupby('attempts').head(2)


# In[226]:

#62. Write a Pandas program to remove first n rows of a given DataFrame. 
Mydat2=Mydat.copy()
Mydat2.iloc[2:,:]


# In[227]:

#63. Write a Pandas program to remove last n rows of a given DataFrame
Mydat2=Mydat.copy()
Mydat2.iloc[:7,:]


# In[ ]:



