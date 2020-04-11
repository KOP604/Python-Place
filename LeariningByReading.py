"""
Created on Mon Sep 23 12:36:18 2019
Misc examples from reading
"""

import pandas as pd
import numpy as np
import datetime as DT

"""
LIST EXPANSION method o create multiple dataframes
"""
df1, df2, df3, df4, df5 = (pd.DataFrame(np.random.randint(0, 1000, (100, 3)))
                           for i in range(5))
#not working
dt=['df1','df2','df3','df4','df5']
for i in [df1, df2, df3, df4, df5]:
    i=pd.DataFrame(np.random.randint(0,1000, (100,3)))

#worked don't know how
d={}
for name in dt:
    d[name]=pd.DataFrame(np.random.randint(0,1000, (100,3)))
    
for key in d.keys():
    print(key)

#imilar to SAS's maceo languange: code that generate code'
for i in range(5):
    print('df'+str(i)+'=pd.DataFrame(np.random.randint(0,1000, (100,3))))')
    


#### Create multipl columns?
# this is OK
df=pd.DataFrame(columns=['v1','v2','v3','v4','v5'])
for i in range(5):
    df.iloc[:,i]=(np.random.randint(0,76,(100,)))
    
df.info()
df[['v1','v2','v3','v4','v5']]

# Create multiple columns using list expansions?
# not working 或方法df1=DataFrame()
不对
df[['v1','v2','v3','v4','v5']]=(np.random.randint(0,76,(100,5)) for i in range(5))
df.tail(10)

#need to learn more about generator
(np.random.randint(0,76,(10,1)) for i in range(3))

"""
Alternatively use dictionary but dataframe is nl[df1] nl[df2]...
"""
nl={}
for i in range(5):
    nl['df'+str(i+1)]=pd.DataFrame(np.random.randint(0,10000,(10000,500)))
    
nl.keys()  
nl.items()
nl['df3'].info()

"""
pd.eval is vectorized operation
"""
result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')

#pd.eval() some advantages in referencing see the examples below
np.allclose(result1, result2)
df = pd.DataFrame(np.random.rand(1000, 3), columns=['A', 'B', 'C'])
result1 = (df['A'] + df['B']) / (df['C'] - 1)
result3 = df.eval("(A + B) / (C - 1)")
result3.sum()

df.eval("New_col=(A + B) / (C - 1)", inplace=True)
df.columns

#DF can commandate elementwise operation 
np.sqrt(df['c'])

New=df['c']*df['k']
New.head(10)


# title?
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

"""
Python built-in function vs. Pandas function
"""
from pandas import *
df1, df2, df3, df4, df5 = (DataFrame(np.random.randint(-1000, 1000, (100, 3)))
                           for i in range(5))
#both OK
df3=df2.abs()
df3=abs(df2)

#  commenting with '"""'
"""
multiple line comments
Python will ignore them
"""

""" 很有用的
以下 LIST method
"""
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
df= pd.DataFrame(np.random.randint(0, 10, (20, 12)), 
                 columns=list('abcdefghijkl'))

df[3] # Does not work w DataFrame
df['h'][3] # works w Series 
df.iloc[3]
df.iloc[3, 2:7]
df.iloc[3:10, 2:7]
df.head(10)

#check if a value exist in a column
-18 in df['f'].values
18 in df['c'].values


4 in df['h'].values
df['h']=df['h'].astype('str')
4 in df['h'].values
'4' in df['h'].values

#isin() and ~isin ()
df['k']
K=(df['k'] not in [10,6,5]) # wrong 
~df['k'].isin ([10,6,5]) #correct
df['k'].isin(df['c']) #correct

Q=[1,3,6,7,9]
Q+Q
Q+2 #not working
Q*2 # same as Q+Q

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

"""
dictionary with ZIP function
"""
old_names=['A','B','C']
new_names=['AA','BB','CC']

df=pd.DataFrame(np.random.random(size=(100,3)), columns=old_names)
df.columns.values

# not working dict([old_names,new_names]) must use zip()
# for example: dict(zip(old_names,new_names)) #zip is pairing
df=df.rename(columns=(dict(zip(old_names,new_names))))
df.columns

"""
Pandas .read_html() function will return a list of dataframes where each dataframe 
is a table found on the page 
"""
file='F://KeyPass-1.23/KeePass 2019-07-09 Database.kdb.html'
html=pd.read_html(file, header=0)    
type(html) # list
len(html)
df=html[0] #hte only table available ofor this html
type(df) #Dataframe

"""
MAP 作为 Pandas  method
相当于 SAS's FORMAT 或者 Excel's vlookup()
FORMAT 还有另外一个匹配 PD.CUT(dat, value format, labels)
"""
#dataframe with 8 observations
df=pd.DataFrame({'state':['MI','MA','MD','MS','MD','PA','DE','NJ'],'val':np.random.randint(0,1000,(8,))})
df
df['region']=df['state'].map({'MD':'NE','DE':'NE','PA':'NE'})
df

#dataframe2 with 9 observations
df2=pd.DataFrame({'state':['MA','MI','DE','MS','PA','MD','NJ','MN','TX'],'rdnum':np.random.random((9,))})
df2
df['vlookup']=df['state'].map(dict(zip(df2['state'],df2['rdnum'])))
df[['state','vlookup']]


除非是INDEX，可以做
ds=pd.Series(index=['MI','MA','MD','MS','MD','PA','DE','NJ'],data=np.random.randint(0,1000,8))
ds2=pd.Series(index=['MI','MA','MD','MS','MD','PA','DE','NJ'],data=range(8))
df=ds.map(ds2)

"""
MAP作为 PYTHON FUNCTION的用法 ******

   
#apply/call a function to an iterable
A=[m,n,p]
map(func, A) ===> f(m),f(n),f(p)

example:
flst=['fi1','fi2','fi3']
map(pd.read_csv, flst) ==> pd.read_csv('fi1'), pd.read_csv('fi2'),,....
"""

"""
注意 ILOC和LOC都可以用INTEGER 但LOC是按LABEL ILOC是按指数
"""

df2.head(10)
df2.loc[5:7,:]
df2.iloc[5:7,:]

"""
how to use set_index and rest_index()
set_index利用现成的COLUMN
reset_index就是归零 恢复用数字INDEX
reindex()就是用新的外在的COL做INDEX
"""
K=list('abcdefghi')
K
df2['new']=K
df2.set_index('new')
df2.reset_index()



"""
bin numeric data
"""
df=pd.DataFrame(np.random.randint(-45,753,(1000,2)), columns=('PO_ID','Age'))
df.loc[2,'Age']=-4
df.head(10)

bins = [-99, 0, 10, 30, 50, np.inf]
#PYTHON的algorithm将这这样划分：-99-0】，0-10】，。。50-NP》INF】 所以注意LABEL的定义
names = ['<0','0-10','10-30','30-50','50+'] #BIN-1
df['AgeRange'] = pd.cut(df['Age'], bins, labels=names,right=False)
df['AgeRange'].value_counts().sort_values()
df.groupby('AgeRange')['Age'].agg(['min', 'max'])

"""
dict() examples DICT里面的KEY不一定非要是STRINg 可以是NUM 如下面所显示
"""
dict(m=8, n=9)
dict(zip(['m','n'],[8,9]))
dict(['m','n'],[8,9]) # not working have to zip them

mylist = list('abcedfghijklmnopqrstuvwxyz') 
mylist=np.arange(26)
myarr = np.arange(26) 
mydict = dict(zip(mylist, myarr))
mydict

"""
关于LAMBDA APPLY LOOPING的思索
凡是要LOOP整个数据时 一定可以用APPLY（某个FUNC）来解决
如果是简单的单变量的FUNC 则一定可以用LAMBDA短函数
"""

"""
取每组的第N个OBS 先把数据按需要SORT 然后用GROUPBY.HEAD(1)取头一个OBS就好。 比如想要每个ID
的头一个DT， 就先SORT BY ID & DT　然后用GROUPBY。ＨＥＡＤ
"""
df=pd.DataFrame({'ID':[11,72,11,72,11], 'DT':[35,91,15,56,23]})
df.sort_values(['ID','DT'])
df.groupby('ID',as_index=False).head(1)
df=df.sort_values(['ID','DT'])
df.groupby('ID',as_index=False).head(1)

df=df.merge(df.groupby('ID',as_index=False).head(1), on=['ID','DT'], how='left', indicator=True)
df['FST']=0
df.loc[df['_merge']=='both', 'FST']=1
df.drop('_merge', axis=1)


# retain cum first last 
df=pd.read_excel('W://DS_PY/dat1.xlsx')
df['NOW']=df['NOW'].astype('float')
df.sort_values(['PO_ID','DT'],inplace=True)

#mark the first and last obs
fst=df.groupby('PO_ID', as_index=False)['DT'].min()
lst=df.groupby('PO_ID', as_index=False)['DT'].max()

fst['FST']=1
df=df.merge(fst, on=['PO_ID','DT'], how='left')
lst['LST']=1
df=df.merge(lst, on=['PO_ID','DT'], how='left')

#identify YR when assts down to 0
df['DN']=0
K=(df['PRR']>0) & (df['NOW']==0) 
df.loc[K,'DN']=1

# find last yr there are assets
K=np.abs(df['PRR'])+np.abs(df['NOW'])>0
fst0=df[K].groupby('PO_ID', as_index=False)['DT'].max()

#mark the obs after the found last year w/ assets
fst0.rename(columns={'DT':'DTT'}, inplace=True)
df=df.merge(fst0, on=('PO_ID'), how='left')
df['Marked']=0
df.loc[(df['DT']>df['DTT']) & (pd.notnull(df['DTT'])),'Marked']=1
df

#reactivated cases assets went down to 0 and then rebound
df.drop(['DTT'], axis=1, inplace=True)

K=(df['PRR']==0) & (df['NOW']>100)
PO=df[K].groupby('PO_ID',as_index=False)['DT'].max()
PO.rename(columns={'DT':'BDT'}, inplace=True)
df.drop('react', axis=1, inplace=True)

#map
df['BDT']=df['PO_ID'].map(dict(zip(PO['PO_ID'],PO['BDT'])))
#or merge  
df=df.merge(PO,on='PO_ID', how='left')
K=(df['DN']==1) & (df['DT']<df['BDT'])
df['react']=0
df.loc[K,'react']=1
df.groupby('PO_ID',as_index=False)['react'].sum()


#cases have many years w/o assets once IN. How to diiferrentiate from
#the many 0 in late stages
df['LATE']=0
df.loc[(df['NOW']==0) & (df['PRR']==0) & (df['DT'].isin([1,2])), 'LATE']=1
df.groupby('PO_ID',as_index=False)['LATE'].sum()


#test str.zfill()
df= pd.DataFrame(np.random.randint(1,1050, (90, 12))*1.0, 
                 columns=list('abcdefghijkl'))
df.dtypes
df[['h','h5']].sample(10)
df['h2']=df['h'].astype('int')
df['h2']=df['h2'].astype('str').str.strip()
df['h2']=df['h2'].str.zfill(5)

df['h5']=df['h'].apply(int).astype('str').str.strip().str.zfill(5)

