# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:52:50 2019


@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as DT


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(data,index=labels)

df.info()
df.head(3)
df[['animal','age']]
df.iloc[:,0:2]
df.iloc[[3,4,8],0:2]

#10 select those age missing
df[df['age'].isnull()]
df[pd.notna(df['age'])]

#11.
K=(df['animal']=='cat') & (df['age']<3)
df[K]

K=(df['age']>=3) & (df['age']<=5)
df[K]

#13
df.loc['f','age']=1.5
df

#14.
df['visits'].sum()

#15
df.groupby('animal')['age'].mean() #不用重复DF

#16
K={'animal':'mouse', 'age': 5, 'visits': 15, 'priority':'no'}
df=df.append(K,ignore_index=True)

df=df.drop(10, axis=0)

#17
df['animal'].value_counts()

#18
df.sort_values(by=('age'), ascending=True)
df.sort_values(by=(['age','visits']), ascending=[True, False])

#19
df["New"]=False
df.loc[df['priority']=="yes", "New"]=True
df["New"]
df.drop('priority', axis=1, inplace=True)
df.rename(columns={'New':"priority"}, inplace=True)
df

#20
df.loc[df['animal']=='snake','animal']='python'
df

#21 
df.groupby(['animal','visits'])['age'].mean()

#22 Intermediate level
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df.duplicated()
df.drop_duplicates(inplace=True)

#23
df = pd.DataFrame(np.random.random(size=(5, 3)))
df_rmean=df.mean(axis=1)
df2=df.copy()

for i in range(5):
    df2.iloc[i,:]=df.iloc[i,:]-df_rmean[i]
    
df2    

#24 Which column of numbers has the smallest sum? (Find that column's label.)
df = pd.DataFrame(np.random.random(size=(5000, 10)), columns=list('abcdefghij'))

K=pd.Series()

for i in df.columns:
    K[i]=df[i].sum()

J=K.min()
K[K==J].index.values

#25
df2=df[17:33]
df=pd.concat([df,df2], axis=0)
len(df)
df.duplicated().sum()
df=df.drop_duplicates()

"""
#26 26. You have a DataFrame that consists of 10 columns of floating--point numbers. 
Suppose that exactly 5 entries in each row are NaN values. For each row of the DataFrame, 
find the column which contains the third NaN value.
"""
df = pd.DataFrame(np.random.random(size=(20, 10)), columns=list('abcdefghij'))

#create 5 NaN for each row
vlst=list('abcdefghij')
def a0(db):
    K=np.random.choice(10, 5, replace=False)
    for i in range(5):
        ME=K[i]
        db[vlst[ME]]=np.nan
    
df.apply(a0,axis=1)
df

def f5(db):
    CNT=0
    for i in vlst[::-1]:
        if pd.isnull(db[i]):
            CNT+=1
            if CNT==1:
                return i
                break
    
df['_5th_NaN']=df.apply(f5,axis=1)
df


K[3]
type(K)
#27  A DataFrame has a column of groups 'grps' and column of numbers 'vals'. 
#For each group, find the sum of the three greatest values.
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df
df.sort_values(by=(["grps","vals"]), ascending=[True, False], inplace=True)
df2=df.groupby("grps")["vals"].nlargest(3)
df2.groupby("grps").sum()

#28
df = pd.DataFrame(np.random.random(size=(50, 10)), columns=list('abcdefghij'))
df['ME']=df.index
df.head(3)
BIN=[0,10,20,30,40,50]
df['grp']=pd.cut(df['ME'], BIN, right=False)
df.tail(10)
df.groupby('grp')['j'].sum()

#29 skip
#30
df = pd.DataFrame(np.random.random(size=(50000, 10)), columns=list('abcdefghij'))
df.shape
df.tail(10
        )

vlst=list('abcdefghij')
Three=pd.DataFrame()

OT=[]
ID=[]
for i in vlst:
    K=df[i].max()
    #Three['Col']=i
    #Three['Val']=K
    #Three['ID']=df[df[i]==K].index.values
    
    ID.append(df[df[i]==K].index.values)
    OT.append(K)
    
HA=pd.DataFrame({'Val':OT, 'ID':ID}, index=vlst)
HA.sort_values(by='Val', ascending=False)

#not the best solution try again
ID=[]
ME=pd.Series()
K=[]
for i in vlst:
    K=df[i].nlargest(3)
    #Three['Col']=i
    #Three['Val']=K
    #Three['ID']=df[df[i]==K].index.values
    
    #ID.append(df[df[i]==K].index.values)
    ME=ME.append(K)
len(ME)
vlst2=vlst*3    
vlst2.sort()
ID=pd.Series(vlst2, index=ME.index)
pd.concat([ME, ID], axis=1) #finally !!

"""
31. Given a DataFrame with a column of group IDs, 'grps', and a column of 
corresponding integer values, 'vals', replace any negative values in 'vals' 
with the group mean
"""
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [12,345,3,-1,45,-14,4,52,54,23,-235,-21,57,3,-87]})
DM=df.groupby('grps')['vals'].mean()
DM
DM=DM.to_frame('mea')
DM['grps']=DM.index
df=pd.merge(df, DM, how='left', on='grps', indicator=True)
K=df['vals']<0
df.loc[K,'vals']=df['mea']
df


"""
32 Implement a rolling mean over groups with window size 3, 
which ignores NaN value. For example consider the following DataFrame:
"""
df = pd.DataFrame({'group': list('aabbabbbabab'),
                       'value': [1, 2, 3, np.nan, 2, 3, 
                                 np.nan, 1, 7, 3, np.nan, 8]})
df['group'].value_counts()    
K=df['group']=='b'
B=df[K & (pd.notnull(df['value']))]
K=df['group']=='a'
A=df[K & (pd.notnull(df['value']))]

AM=A['value'].rolling(3).mean()
BM=B['value'].rolling(3).mean()

df=pd.concat([df, AM.to_frame("Avalue")], join='outer', axis=1)
df=pd.concat([df, BM.to_frame("Bvalue")], join='outer', axis=1)
df

"""
DateTime excercises
33. Create a DatetimeIndex that contains each business day of 2015 
and use it to index a Series of random numbers, s.
"""
S = pd.Series(np.random.random(261),index=pd.bdate_range(start='1/1/2015', end='12/31/2015'))
S.index

"""
34. Find the sum of the values in S for every Wednesday.
"""
S[S.index.dayofweek==3].sum()

"""
#35. For each calendar month in s, find the mean of values
"""
SV['WK']=SV['DT'].dt.week
SV['WK'].tail(10)

SV.groupby(SV['DT'].dt.week)['Val'].mean()

"""
36. For each group of four consecutive calendar months in s, 
find the date on which the highest value occurred.
"""
D=SV.groupby(SV['DT'].dt.month)['Val'].nlargest(1) 
"""
注意nlargest是REC水平操作因此保留ID，如果是MAX就是综合操作不保留ID
"""

K=list(D.rolling(4).max().index.values)
for i in range(12):
    print(SV.loc[K[i][1], 'DT'])

"""
#37   
Create a DateTimeIndex consisting of the third Thursday in each month for the 
years 2015 and 2016.
"""
SV = pd.DataFrame({'DT': pd.date_range(start='1/1/2015', end='12/31/2015'), 
                 'Val':  np.random.random(365)})

SV['DOW']=SV['DT'].dt.dayofweek
SV['MN']=SV['DT'].dt.month
K=SV['DOW']==3
W=SV[K].groupby('MN').nth(2)
SV2=pd.DatetimeIndex(W['DT'])      
SV2

#38 clean data: replace missing by lagged record
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
                               '12. Air France', '"Swiss Air"']})

df['F2']=df['FlightNumber'].shift()+10

#1. Vectorized Solution
df['FlightNumber'].replace(np.nan, df['F2'], inplace=True)
df['FlightNumber'].fillna(df['F2'], inplace=True)


#2.use apply
def fln(db):
    if pd.isnull(db['FlightNumber']):
        return db['F2']
    else:
        return db['FlightNumber']

df['F3']=df.apply(fln,axis=1)
df[['F3','FlightNumber']]

#3.use db.loc[]
K=pd.isnull(df['FlightNumber'])
df['F3']=df['FlightNumber']
df.loc[K,'F3']=df['F2']
df

"""
#39 The From_To column would be better as two separate columns! 
Split each string on the underscore delimiter _ to give a new temporary 
DataFrame with the correct values. Assign the correct column names to 
this temporary DataFrame.
"""

df['From']=df['From_To'].str.split("_").str.get(0)
df['To']=df['From_To'].str.split("_").str.get(1)
df

"""
#40 Notice how the capitalisation of the city names is all mixed up 
in this temporary DataFrame. Standardise the strings so that only 
the first letter is uppercase (e.g. "londON" should become "London".)
"""
df['From']=df['From'].str.capitalize()
df['To']=df['To'].str.capitalize()

"""
#41 skip
#42 In the Airline column, you can see some extra puctuation 
#and symbols have appeared around the airline names. Pull out 
#just the airline name. E.g. '(British Airways. )' should 
#become 'British Airways'.
"""

df['Plane']=df['Airline'].str.replace('\d',' ')
df['Plane']=df['Plane'].str.replace('\W',' ').str.strip()
df

"""
43.
"""
df=pd.concat([df, df['RecentDelays'].apply(pd.Series)],axis=1)
df.rename(columns={0:'Delay1',1:'Delay2',2:'Delay3'}, inplace=True)
df.rename(columns={'RecentDelays':'Delays'}, inplace=True)
df

"""
skipped multiindex section
51 
"""
df=pd.DataFrame({'x':[0,1,2,3,4]*4, 'y':[0,1,2,3]*5})
df.sort_values(['x','y'], inplace=True)
df["Odd"]=(np.random.random(size=(20))>=.6)*1
df["Odd"].value_counts()


"""
53. Now create a new column for this DataFrame called 'adjacent'. This column should 
contain the number of mines found on adjacent squares in the grid.
(E.g. for the first row, which is the entry for the coordinate (0, 0), 
count how many mines are found on the coordinates (0, 1), (1, 0) and (1, 1).)
"""

"""
关键问题是APPLY（）不能进行VECTOR WIDE操作
def minesweep(db,col1,col2):
        i=db[col1]
        j=db[col2]
        K=db.loc[(abs(db[col1]-i)<=1) & (abs(db[col2]-j)<=1),'Odd'].sum() - db.loc[(db[col1]==i) & (db[col2]==j),'Odd'].sum()
        return K
"""
df['adjcnt']=0

for i in [0,1,2,3,4]:
    for j in [0,1,2,3]:
        df.loc[(df['x']==i) & (df['y']==j),'adjcnt']=db.loc[(abs(db['x']-i)<=1) & (abs(db['y']-j)<=1),'Odd'].sum() - db.loc[(db['x']==i) & (db['y']==j),'Odd'].sum()
    
df
        
#54. For rows of the DataFrame that contain a mine, set the value in the 'adjacent' column to NaN.
df.loc[df["Odd"]==1, "adjcnt"]=np.nan
df


"""      
#55 Finally, convert the DataFrame to grid of the adjacent mine counts: 
columns are the x coordinate, rows are the y coordinate.
"""
df.pivot(index='y', columns='x', values='adjcnt')       

"""
PLOTTING
"""
#import matplotlib.pyplot as plt
plt.style.use('ggplot')

#56 make a scatter plot of this random data, but use black X's instead of the default markers.
df = pd.DataFrame({"xs":[1,5,2,8,1], "ys":[4,2,1,9,6]})
df.plot.scatter('xs','ys', markersize=8) # marker not working
plt.scatter('xs','ys',data=df, marker=8)

"""
57. Columns in your DataFrame can also be used to modify colors and sizes. 
Bill has been keeping track of his performance at work over time, as well as 
how good he was feeling that day, and whether he had a cup of coffee in 
the morning. Make a plot which incorporates all four features of 
this DataFrame.
"""
df = pd.DataFrame({"productivity":[5,2,3,1,4,5,6,7,8,3,4,8,9],
                   "hours_in"    :[1,9,6,5,3,9,2,9,1,7,4,2,2],
                   "happiness"   :[2,1,3,2,3,1,2,3,1,2,2,1,3],
                   "caffienated" :[0,0,1,1,0,0,0,0,1,1,0,1,0]})
    
df['x']=df.index

plt.plot('x', 'productivity', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot('x', 'hours_in', data=df, marker='', color='olive', linewidth=2)
plt.plot('x', 'happiness', data=df, marker='', color='olive', linewidth=6, linestyle='dashed', label="toto")

"""
58 Make a bar plot of monthly revenue with a line plot of monthly advertising 
spending (numbers in millions)
"""
df = pd.DataFrame({"revenue":[57,68,63,71,72,90,80,62,59,51,47,52],
                   "advertising":[2.1,1.9,2.7,3.0,3.6,3.2,2.7,2.4,1.8,1.6,1.3,1.9],
                   "month":range(12)
                  })
df['F10']=df['advertising']*10
    
ax=plt.gca()
df.plot(x='month', y='revenue',kind='line',linestyle='-', ax=ax, color='red')
df.plot(x='month',y='advertising', kind='bar',ax=ax, color='green')
df.plot(x='advertising',y='revenue', kind='scatter', color='blue')

"""
#58 stock chart We would like each candle to represent an hour's worth of data. 
You can write your own aggregation function which returns 
the open/high/low/close, but pandas has a built-in which also does this.
"""
df=pd.DataFrame()
def float_to_time(x):
    return str(int(x)) + ":" + str(int(x%1 * 60)).zfill(2) + ":" + str(int(x*60 % 1 * 60)).zfill(2)

def day_stock_data():
    #NYSE is open from 9:30 to 4:00
    time = 9.5
    price = 100
    results = [(float_to_time(time), price)]
    while time < 16:
        elapsed = np.random.exponential(.001)
        time += elapsed
        if time > 16:
            break
        price_diff = np.random.uniform(.999, 1.001)
        price *= price_diff
        results.append((float_to_time(time), price))
    
    
    df = pd.DataFrame(results, columns = ['time','price'])
    df.time = pd.to_datetime(df.time)
    return df

df=day_stock_data()
df.sort_values('time')
high=df.groupby(df['time'].dt.hour)['price'].nlargest(1)
low=df.groupby(df['time'].dt.hour)['price'].nsmallest(1)
OPEN=df.groupby(df['time'].dt.hour)['price'].first()
close=df.groupby(df['time'].dt.hour)['price'].last()

K=list(range(9,16))
high.index=K
low.index=K
OPEN.index=K
close.index=K

"""## combine series into dataframe 
NOTE NOTE NOTE: all series have to be properly indexed
"""
# method 1
agg=pd.DataFrame(columns=['high','low'])
agg['high']=high
agg['low']=low
agg

#method 2
agg=pd.DataFrame({'high':high, 'low':low, 'open':OPEN, 'close':close},index=high.index)
agg


"""
agg is a DataFrame which has a DatetimeIndex and five columns: ["open","high","low","close","color"]
"""
def plot_candlestick(agg):
    """
    agg is a DataFrame which has a DatetimeIndex and five columns: ["open","high","low","close","color"]
    """
    fig, ax = plt.subplots()
    for time in agg.index:
        ax.plot([time.hour] * 2, agg.loc[time, ["high","low"]].values, color = "black")
        ax.plot([time.hour] * 2, agg.loc[time, ["open","close"]].values, color = agg.loc[time, "color"], linewidth = 10)

    ax.set_xlim((8,16))
    ax.set_ylabel("Price")
    ax.set_xlabel("Hour")
    ax.set_title("OHLC of Stock Value During Trading Day")
    plt.show()

plot_candlestick(agg)


def plot_candlestick(agg):
    """
    agg is a DataFrame which has a DatetimeIndex and five columns: ["open","high","low","close","color"]
    """
    fig, ax = plt.subplots()
    for time in agg.index:
        ax.plot([time] * 2, agg.loc[time, ["high","low"]].values, color = "black")
        ax.plot([time] * 2, agg.loc[time, ["open","close"]].values, color = 'red', linewidth = 10)

    ax.set_xlim((8,16))
    ax.set_ylabel("Price")
    ax.set_xlabel("Hour")
    ax.set_title("OHLC of Stock Value During Trading Day")
    plt.show()

import plotly.graph_objects as go #did not install successfully
fig = go.Figure(data=[go.Candlestick(x=agg.index,
                open=agg['open'],
                high=agg['high'],
                low=agg['low'],
                close=agg['close'])])

fig.show()