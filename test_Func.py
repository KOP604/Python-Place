# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:33:54 2019
How to bring arguments to user-defined function - PL
@author: Administrator
"""

import pandas as pd
import numpy as np
import datetime as DT

movies=pd.read_csv("D://Python/Data/movies_data.csv")
DIC=pd.read_csv("D://Python/Data/movies_metadata.csv")
movies.shape
movies.columns
movies['production_companies'].nunique()
movies['popularity'].nunique()
movies['adult'].nunique()
movies['adult'].value_counts()
movies['status'].value_counts()
movies["revenue"].mean()

#
def MyFunc(db):
    if db["status"] == 'In Production':
        return 1
    else:
        return 0

movies["If_Prod"]=movies.apply(MyFunc, axis=1)    

##
def MyFunc2(col):
    if col == 'In Production':
        return 1
    else:
        return 0
    
movies["If_Prod"]=movies["status"].apply(MyFunc2)
WHAT IF I do
movies["If_Prod"]=movie.apply(MyFunc, col='status')


###
def MyFunc3(col):
    if col in ('In Production', 'Planned'):
        return 1
    else:
        return 0
    
movies["DP"]=movies["status"].apply(MyFunc3)    


”“”
vec 表示有多个参数从LIST读取
“”“

def MyFunc4(vec): 
    col1=vec[0]
    col2=vec[1]
    if col1 in ('In Production', 'Released') and (col2>30000000):
        return 1
    else:
        return 0

movies['NewCol'] = movies[['status', 'revenue']].apply(MyFunc4, axis=1)


#####
movies['status'].value_counts()

"""
或者直接定义多个参数
"""

def MyFunc5(col1,col2):
    if col1 == col2:
        return 1
    else:
        return 0
    
movies['NewCol'] = movies['status'].apply(MyFunc5, col2='Released')


movies['NewCol'].sum()
movies['NewCol']=0
movies.loc[movies['status']=='Released','NewCol']=1

#note the difference between function 6 and function 62
def MyFunc6(vec,col3):
    col1=vec[0]
    col2=vec[1]
    if col1 == col3 and col2>30000000:
        return 1
    else:
        return 0
    
movies['NewCol'] = movies[['status', 'revenue']].apply(MyFunc6, col3='Released',axis=1)

def MyFunc62(db, col1,col2,col3):
    if db[col1] == col3 and db[col2]>30000000:
        return 1
    else:
        return 0
    
movies['NewCol'] = movies.apply(MyFunc62, col1='status',col2='revenue',col3='Released',axis=1)


#validation
movies['NewCol']=0
movies.loc[(movies['status']=='Released') & (movies['revenue']>30000000),'NewCol']=1


def MyFunc7(db,vec,col3):
    col1=vec[0]
    col2=vec[1]
    if db[col1] == col3 and db[col2]>30000000:
        return 1
    else:
        return 0
    
movies['NewCol'] = movies.apply(MyFunc7, vec=['status', 'revenue'], col3='Released',axis=1)


def MyFunc8(db,col1,col2,col3):
    if db[col1] == col3 and db[col2]>30000000:
        return 1
    else:
        return 0

movies['NewCol'] = movies.apply(MyFunc8, col1='status', col2='revenue', col3='Released',axis=1)

#########################################
### conclusion the standard
#########################################
def dbfunc (db,x,y,z,...): # db -dataframe, x,y - columns, z - string/value
    condition db[x].. and db[y]==z and ...
    ...
    
db['NewCol']=db.apply(dbfunc, x='', y='', z='',... axis=1)

#digest this one isin and not in
criterion = lambda row: row['countries'] not in countries
not_in = df[df.apply(criterion, axis=1)]

    