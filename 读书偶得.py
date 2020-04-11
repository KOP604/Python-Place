"""
Created on Mon Sep 23 12:36:18 2019
Misc examples from reading
"""

import pandas as pd
import numpy as np
import datetime as DT

df1, df2, df3, df4, df5 = (pd.DataFrame(np.random.randint(0, 1000, (100, 3)))
                           for i in range(5))

result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')

np.allclose(result1, result2)
df = pd.DataFrame(np.random.rand(1000, 3), columns=['A', 'B', 'C'])
result1 = (df['A'] + df['B']) / (df['C'] - 1)

result3 = df.eval("(A + B) / (C - 1)")
result3.sum()

df.eval("New_col=(A + B) / (C - 1)", inplace=True)
df.columns

df= pd.DataFrame(np.random.randint(-1000, 1000, (900, 12)), 
                 columns=list('abcdefghijkl'))

df.head(10)
df['g'].plot.hist()
K=pd.Series(np.random.randn(12000))
K.plot.hist()
K.sum()
pd.cut(K, bins=7).value_counts().sort_index()
c=K>-1
pd.cut(K[c], [-5,-4,-3,-2,-1, 0,1,2,3,4,5]).value_counts().sort_index()
J=pd.cut(K, [-5,-4,-3,-2,-1, 0,1,2,3,4,5]).value_counts()/12000
J.sort_index().map(lambda n: '{:,.2%}'.format(n))

#Python built-in function and Pandas function
from pandas import *
df1, df2, df3, df4, df5 = (DataFrame(np.random.randint(-1000, 1000, (100, 3)))
                           for i in range(5))

#both OK
df3=df2.abs()
df3=abs(df2)

#commenting
#do something
"""
multiple line comments
Python will ignore them
"""
#LIST method
K=list('abcdefghijkl')
K.pop(2) #'c'
K #'abdefghijkl'

K.index('g')
K.append('Hello')
K

#list comprehension
Mylst=[num1 for num1 in range(1000) if (num1 % 3 ==0) & (num1 % 5==0)]
len(Mylst)
Mylst[:15]

#list slicing w Stride
Mylst=[num1 for num1 in range(100) if (num1 % 5==0)]
Mylst[0:15:2]
Mylst[::2]

#Accessing string element
'abcdefghijkl'[5] #'f'
 
#retrieve rows
df= pd.DataFrame(np.random.randint(-20, 20, (90, 12)), 
                 columns=list('abcdefghijkl'))

df[3] # Does not work w DataFrame
df['h'][3] # works w Series 
df.iloc[3]
df.iloc[3, 2:7]
df.iloc[3:10, 2:7]

#check if a value exist in a column
-18 in df['f'].values
18 in df['c'].values

-18 in df[['f','c']].values

#isin() and in ()
df.head(13)
K=(df['k'] not in [10, 7, 5]) # wrong 
df['k'].isin([10, 7, 5]) #correct
df['k'].isin(df['c']) #correct

Q=[1,3,6,7,9]
Q+Q
Q
Q+2 #not working
Q*2
#DF can commandate elementwise operation 
np.sqrt(df['c'])

#
New=df['c']*df['k']
New.head(10)

#df.plot() method
movies=pd.read_csv("D://Python/Data/movies_data.csv")
movies.info()

import matplotlib.pyplot as plt
plt.style.available
plt.style.use('dark_background')
H=movies['status'].value_counts()/len(movies)*100
H.plot.barh()
movies['status'].value_counts().plot.line()
movies['status'].value_counts().plot()
movies['status'].value_counts().plot.pie()
movies[2:5]
movies[2]
movies.iloc[2]
movies.iloc[2,:]

import seaborn as sns
sns.

a = 'is' 
b = 'nice' 
my_list = ['my', 'list', a, b] 

my_list.index(a)
my_list.count(a)
my_list.index('my')
my_list.reverse()
my_list
my_list.append('!')
my_list.insert(0,'!') 
