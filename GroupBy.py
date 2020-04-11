# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:13:40 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import datetime as dt


test=pd.DataFrame({"uid":['a','b','b','d','e'], "amt":[12,34,56,91,12]})
test['amt'].duplicated()
test.drop_duplicates('amt',inplace=True) #remove one keep one
test

Mydt=dt.date(1997,9,1)
Mydt
Mydt>="1997-10-01"  #Cannot compare type 'Timestamp' with type 'str'
Mydt>=pd.Timestamp("1994-10-01")

#but we can always compare str date w format "YYYY-MM-DD"

kop=[0,2,3,7,8,109,54]
pd.Series(kop)
kopS=pd.Series(kop)
kopS=pd.Series(kop)

#use pandas method
refDt=pd.to_datetime('1951-10-31')
refDt

#use Python built-in module
refDt=dt.datetime(1951,10,31)
refDt
refDt.year

mydt=pd.Timestamp('1995-10-31') #Pandas's timestamp is more flexible than datetime

if mydt.year>refDt.year:
    print('Y')
else:
    print('N')
    

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

chipo.columns

chipo.info()
chipo['priceN']=chipo['item_price'].str.replace('$','').astype(float)

chipo['priceN'].head(5)

# create groupby object 
chipo['item_name'].nunique()
chipo['quantity'].sum()
chipo['priceN'].sum()/chipo['quantity'].sum()


item=chipo.groupby('item_name')
len(item)
item.size().sort_values(ascending=False)

#calculate group stats
item['quantity'].sum().sort_values(ascending=False).head(5)
item.agg({'quantity':['size','sum','mean','max'], 'priceN':'mean'})


#iterate over the groupby object
item_max=pd.DataFrame(columns=chipo.columns)
item_max

for i, data in item:  # i represents group data represents records in each group
#for groupby object iteration need to use two parameters
    M=data.nlargest(1,'quantity')  
    item_max=item_max.append(M)   #append assign to the same dataFrame
    
item_max





    










