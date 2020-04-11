# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:25:08 2019

@author: PL
"""
import pandas as pd
import numpy as np
import datetime as dt

#1 skip
#2.create pd.series from each of the following sources
mylist = list('abcedfghijklmnopqrstuvwxyz') 
myarr = np.arange(26) 
mydict = dict(zip(mylist, myarr))

S1=pd.Series(mylist)
S2=pd.Series(myarr)
S3=pd.Series(mydict)

#3.Convert ser into a dataframe with its index as another column on the dataframe.
mylist = list('abcedfghijklmnopqrstuvwxyz') 
myarr = np.arange(26) 
mydict = dict(zip(mylist, myarr)) 
ser = pd.Series(mydict)
df=ser.to_frame('B').reset_index()
df

#5. assign a name to index
ser = pd.Series(list("abcedfghijklmnopqrstuvwxyz"))
ser.index.name='foo'
ser


#6 From ser1 remove items present in ser2.
ser1 = pd.Series([1, 2, 3, 4, 5]) 
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1[~ser1.isin(ser2)]


#7.Get all items of ser1 and ser2 not common to both.
ser1 = pd.Series([1, 2, 3, 4, 5]) 
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1[~ser1.isin(ser2)]
ser2[~ser2.isin(ser1)]
       
        
#8,Compute the minimum, 25th percentile, median, 75th, and maximum of ser.
ser = pd.Series(np.random.normal(10, 5, 25))
ser.quantile([0,0.25,.75,1])


#9. Calculte the frequency counts of each unique value ser.
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
type(ser)
ser.value_counts()
ser.nunique()

#10 From ser, keep the top 2 most frequent items as it is and 
#replace everything else as ‘Other’.
ser = pd.Series(np.random.randint(1, 5, [312]))
S1=ser.value_counts() # series
X=S1.nlargest(2).index.values.tolist()
ser[~ser.isin(X)]="Other"
ser.sample(20)

#11.Bin the series ser into 10 equal deciles and 
#replace the values with the bin name
ser = pd.Series(np.random.random(200))
ser.sample(10)
ser1=pd.qcut(ser,10, labels=["Dec0","Dec1", "Dec2","Dec3","Dec4","Dec5","Dec6","Dec7","Dec8","Dec9"])
ser1.head(10)
ser1.value_counts().sort_values(ascending=False)


#locate the min and max for each categoy defined by qcut
D1=ser.groupby(ser1).agg(["count","mean"]) #beautiful
type(D1)
D1.rename(columns={"count":"FREQ", "mean":"Avg"}, inplace=True)
D1.index.name="Decile"
D1.rename(index={"Decile":"DECILE"},inplace=True)
D1


#12.Reshape the series ser into a dataframe with 7 rows and 5 columns
ser=pd.Series(np.random.randint(1,10,35))
ser2=ser.reshape(7,5)
DF1=pd.DataFrame(ser2)
DF1

#13 Find the positions of numbers that are multiples of 3 from ser
#这个例子没有用TOLIST（）。INDEX的方法因为有多个SER%3的值相同 PYTHON CONFUSED
ser = pd.Series(np.random.randint(1, 10, 7))
ser

K=0
for i in ser:
     if (i % 3)==0:
         print(K)
     else:
         print("Missed")
     K+=1
         
         
#14 extract the values from ser at positions in POS
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz')) 
pos = [0, 4, 8, 14, 20]
ser[pos]

#15 append and merge
ser1 = pd.Series(range(5)) 
ser2 = pd.Series(list('abcde'))

DF1=pd.concat([ser1,ser2], axis=1)
DF1
DF2=pd.concat([ser1,ser2], axis=0)
DF2

#16 Get the positions of items of ser2 in ser1 as a list.
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13]) 
ser2 = pd.Series([1, 3, 10, 13])

#test             
ser1.tolist().index(3)

fndme=[]
for i in ser2:
    fndme.append(ser1.tolist().index(i))
fndme            


#17 Compute the mean squared error of truth and pred serie            
truth = pd.Series(range(10)) 
pred = pd.Series(range(10)) + np.random.random(10)

import math
truth.var()/math.sqrt(len(truth))
pred.var()/math.sqrt(len(pred))


#18 Change the first character of each word to upper case 
#in each word of ser.
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
for i in range(4):
   ser[i]=ser[i].title()

# define a function and use APPLY()? 
def capt(i):
    return i.title()

ser.apply(capt)

#19 calculate the number of characters in each word 
#in a series? series? 
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
len(ser[2])
for i in range(0,len(ser)):
    K=len(ser[i])
    print(str(K) + "-----" + ser[i])

def wl(i):
    return len(i)
    
ser.apply(wl)

#20 Difference of differences between the consequtive numbers of ser
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
ser.diff()
ser2=ser.diff()
ser2.diff()

#convert a series of date-strings to a timeseries
ser=pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
len(ser)
pd.Timestamp(ser[1])
pd.Timestamp(ser[5])

s3=pd.Series([1,2,3,4,5])
s3

for i in range(0,5):
    s3[i]=pd.Timestamp(ser[i])
    
s3

#22 Get the day of month, week number, day of year and day of week from ser.
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120313', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
ex=pd.Timestamp(ser[2])
ex.year
ex.dayofyear
ex.dayofweek
ex.weekofyear
ex.strftime('%A')
ex.day

for i in range(0,6):
    s=pd.Timestamp(ser[i])
    K=[s.year, s.dayofyear, s.dayofweek, s.weekofyear, s.strftime('%A')]
    print(K)
    

#23.convert year-month string to dates 
#corresponding to the 4th day of the month
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
for i in range(0,3):
    s=pd.Timestamp(ser[i])
    K=dt.date(s.year, s.month, 4)
    print(K)
    

#24. filter words that contain atleast 2 vowels from a series 
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
ser=ser.str.upper()
K=ser.str.find("A") >-1)*1 + (ser.str.find("E") >-1)*1 \
     +(ser.str.find("I") >-1)*1 + (ser.str.find("O") >-1)*1 \
     +(ser.str.find("U") >-1)*1
list(K) 
ser[[0,1,4]]     

#25 Extract the valid emails from the series emails
emails = pd.Series(['buying books at amazom.com (http://amazom.com)', 'rameses@egypt.c om', 'matt@t.co', 'narendra@modi.com']) 
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
emails2=emails.str.strip()
emails2=emails2.str.replace(" ", "") #strip does not work with white spces in the middle

emails2[(emails2.str.find("@")>-1) & (emails2.str.find(".")>-1)]

#26 get the mean of a series grouped by another 
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10)) 
fruit
weights = pd.Series(np.linspace(1, 10, 10)) 
weights
print(weights.tolist()) 
print(fruit.tolist()) #> 

fruit.nunique()
fruit.value_counts()     

df=pd.concat([fruit, weights], axis=1)
df.rename(columns={0:'Fruit',1:'Weight'}, inplace=True)
df.groupby("Fruit")["Weight"].mean()

27. How to compute the euclidean distance between two series
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

tot=0
for i in range(0,10):
    tot+=p[i]**2+q[i]**2
(tot/10)**.5

#28 Get the positions of peaks (values surrounded by smaller values on both sides) in ser.
ser = pd.Series Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

#33 Import every 50th row of BostonHousing dataset (
file="https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
boston=pd.read_csv(file)
def e50(index):
    if index % 50 == 0:
        return False
    else:
        return True

boston2=pd.read_csv(file, skiprows=lambda x: e50(x))
    

#34 importing change the 'medv' (median house value) column 
#so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.
boston['medv'].sample(n=10)
K=boston['medv']>25
boston['medvC']='Low'
boston.loc[K, 'medvC']='High'
boston['medvC'].nunique()
boston['medvC'].value_counts()

#35
#36019/1/20 101 Pandas Exercises for Data Analysis – Machine Learning Plus

#36 Import ‘crim’ and ‘medv’ columns of the BostonHousing datase
cols=['crim','medv']
boston3=pd.read_csv(file, usecols=cols)

#37 # Get the number of rows, columns, datatype and summary statistics 
# of each column of the Cars93 
# Also get the numpy array and list equivalent of the dataframe.
file='https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
Cars93=pd.read_csv(file)
Cars93.shape
Cars93.dtypes
Cars93.describe()


# 38 Which manufacturer, model and type has the 
# highest Price? What is the row and column number of the cell 
#with the highest Price value?

K=Cars93['Price']==Cars93['Price'].max()
Cars93.loc[K,['Manufacturer','Model','Type','Price']].index.values

#39 Rename the column Type as CarType in df and replace the ‘.’ in column names with ‘_’.
Cars93=Cars93.rename(columns=({"Type":"CarType"}))
K=list(Cars93.columns)
for i in range(0,len(K)):
    haha=K[i].find('.')
    if haha>-1:
        K[i]=K[i].replace('.','_') 

Cars93.columns=K
Cars93.columns

########################################
Cars93_2=Cars93.copy()
########################################
#40. check if a dataframe has any missing values? 
Cars93_2.isnull().any()

#41. How to count the number of missing values in EACH COLUMN
Cars93_2.isnull().sum()

#43 Replace missing values in Min.Price and Max.Price columns with 
# their respective mean
AVP=Cars93_2["Min_Price"].mean()
AVP2=Cars93_2["Max_Price"].mean()

#FILLNA
Cars93_2["Min_Price"].fillna(AVP, inplace=True)
Cars93_2["Max_Price"].fillna(AVP2, inplace=True)

#REPLACE
Cars93_2["Max_Price"].replace(np.nan, AVP, inplace=True)
Cars93_2["Max_Price"].replace(np.nan, AVP2, inplace=True)

#OR Cars93["Max_Price"]=Cars93["Max_Price"].replace(np.nan, AVP2)

#use filter
Mask=Cars93_2["Min_Price"].isnull()
Cars93_2["Min_Price"]=Cars93_2.loc[Mask, "Min_Price"]=AVP
Mask2=Cars93_2["Max.Price"].isnull()
Cars93_2["Max_Price"]=Cars93_2.loc[Mask, "Max_Price"]=AVP2

Mask=Cars93_2["Min_Price"].isnull()
ME=Cars93_2.index[Mask]
Cars93_2["Min_Price"].isnull().sum()
Cars93_2.loc[ME,'Min_Price']=AVP

#43 use apply() to replace missing values
def fillmiss (x):
     if pd.isnull(x):
        return AVP
     else:
        return x 
    
#Min_Price=Cars93_2['Min.Price'].to_frame("Min_Price")
Cars93_2['Min_Price'].isnull().sum()
Cars93_2['Min_Price']=Cars93_2['Min_Price'].apply(fillmiss)
Cars93_2['Min_Price'].isnull().sum()

#Alternatively use Lambda
Cars93_2['Min.Price']=Cars93_2['Min.Price'].apply(lambda x: AVP if pd.isnull(x) else x)

#44 How to select a specific column 
# from a dataframe as a dataframe instead of a series? 
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df.head(5)
a_col=df['a'].to_frame()

#45  How to change the order of columns of a dataframe? 
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df.columns

#45.1 interchange columns 'a' and 'c'
df
df_1=df[list('bacde')]
df_1

#45.2 Create a generic function to interchange two columns, without 
# hardcoding column names.

df.columns.get_loc("c")
vlst=list('abcde')
vlst.index('c')


def tc (x,y):
    vlst=list('abcde')
    i=vlst.index(x)
    j=vlst.index(y)
    vlst[i]=y
    vlst[j]=x   
    
tc(x="d",y="c")     
vlst

df_1=df[vlst]
df_1.columns

#45.3 Sort the columns in reverse alphabetical order, that is colume
#'e' first through column 'a' last.
df_1=df.sort_index(axis=1, ascending=False) #goody!


# 46 printing the dataframe df it shows a maximum of 10 rows 
# and 10 columns.

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
Cars93

#47 Suppress scientific notations like ‘e-03’ in df 
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df1=df.round(4)
df1

#48 format all the values in a dataframe as percentages

df1['Pct']=df1['random']*100
df1['Pct'].astype(str)+"%"

# 49 filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)
Cars93.columns
Cars93.loc[0::20,['Manufacturer', 'Model', 'Type']]

#50 Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' 
# and 'Type' and create a index as a combination of these three 
#columns and check if the index is a primary key

Cars93_2=Cars93.copy()
Cars93_2["Manufacturer"].fillna('missing', inplace=True)
Cars93_2["Model"].fillna('missing', inplace=True)
Cars93_2["Type"].fillna('missing', inplace=True)
Cars93_2.rename(columns={'CarType':'Type'}, inplace=True)
Cars93_2.columns
Cars93_2.set_index(Cars93_2["Manufacturer"]+"_"+Cars93_2["Model"]+"_"+Cars93_2["Type"], inplace=True)
Cars93_2.index

#51 Find the row position of the 5th largest value of column 'a' in df.
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))
K=df.sort_values(by="a",ascending=False).head(5)
K.index.values.tolist()[4]

#52 In ser, find the position of the 2nd largest value greater than 
#the mean.
ser = pd.Series(np.random.randint(1, 100, 15))
K=ser/ser.mean()
KK=K.sort_values(ascending=False)
KK.index.values[4]

#53 Get the last two rows of df whose row sum is greater than 100
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
K=df.sum(axis=1)
K.sort_index(ascending=False, inplace=True)
K[K>100].index.values[[0,1]]

#Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 
#5th and 95th %ile value.
ser = pd.Series(np.logspace(-2, 2, 30))
L=ser.quantile(.05)
U=ser.quantile(.95)
ser[ser>U]=U
ser[ser<L]=L

#55 Reshape df to the largest possible square with negative values removed.
#Drop the smallest values if need be. The order of the positive numbers in 
#the result should remain the same as the original

df = pd.DataFrame DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))


#56 Swap rows 1 and 2 in df.
df = pd.DataFrame(np.arange(25).reshape(5, -1))
r1=df.iloc[0,:].tolist()
r2=df.iloc[1,:].tolist()
df.iloc[0,:]=r2
df.iloc[1,:]=r1
df

#57 Reverse all the rows of dataframe df
df = pd.DataFrame(np.arange(25).reshape(5, -1))
df.sort_index(ascending=False, inplace=True)
df.reset_index(inplace=True)
df.index.values

#58 dummy coding
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
df
DM=pd.get_dummies(df['a'])
pd.merge(df, DM, how='left', left_index=True, right_index=True)                            

#59 Obtain the column name with the highest number of 
#row-wise maximum’s in df.
df=pd.DataFrame(np.random.randint(1,40, 100).reshape(20,-1))
df.columns=list('abcde')

looksee=df.sum(axis=1).max()
ROW=df.loc[df.sum(axis=1)==looksee,:]
MAXV=ROW.max(axis=1).tolist()
RLOC=ROW.max(axis=1).index.tolist()
df.iloc[RLOC[0],:]

for i in range(5):
    if df.iloc[RLOC[0],i] == MAXV[0]:
        print (i)
    else:
        print("No!")
        

#60 Create a new column such that, each row contains the row 
# number of nearest row-record by euclidean distance.
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), 
                            columns=list('pqrs'), index=list('abcdefghij')) 
df
example=df.iloc[0:2,]
example    

zc=0
base=0
whichrow='start'
for a in range(10):
    for b in range(10):
        for i in range(4):
            if a !=b:
                zc=(df.iloc[a,i]-df.iloc[b,i])**2
                if base<zc:
                    whichrow=df.index.values[b]
                    base=zc
    print(whichrow)
    J=df.index.values[a]
    df.loc[J,'EU']=whichrow
    base=0
df
 #later learn how to use iterrows()       
next(df.iterrows())[0]


#61 Compute maximum possible absolute correlation value of 
# each column against other columns in df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), 
                  columns=list('pqrstuvwxy'), 
                  index=list('abcdefgh'))
VL=list('pqrstuvwxy')
for i in range(len(VL)):
    MEtwo=0
    for j in range(len(VL)):
        K=np.abs(df[VL[i]]-df[VL[j]]).sum()
        if MEtwo<K:
            MEtwo=K
            WHO=VL[j]
    print(VL[i],WHO,MEtwo)
    
#62 Compute the minimum-by-maximum for every row of df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

#63 Create a new column 'penultimate' 
#which has the second largest value of each row of df
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), 
                  columns=list('pqrstuvwxy'))
                  , 
                  index=list('abcdefgh'))
df['MAX']=df.max(axis=1)
q=list('abcdefgh')
for x in range(len(df)):
    MIN=-100
    for i in range(10):
        K=df.iloc[x,i]-df.loc[q[x],'MAX']
        #print(K)
        if (MIN<K) & (K !=0):
            MIN=K
            a=x
            b=i
    print(q[x],df.iloc[a,b])

#APPLY
df
.shape
q
q=list('pqrstuvwxy')

def per(db):
    MIN=-100
    for i in range(10):
        K=db[q[i]]-db['MAX']
        if (MIN<K) & (K !=0):
            MIN=K                
            b=i
    return db[q[b]]

df['Perultimate']=df.apply(per,axis=1)
df
   
#64 Normalize all columns of df by subtracting the column mean 
#and divide by standard deviation. 2. 
#Range all columns of df such that the minimum value in each 
#column is 0 and max is 1.

df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1),columns=list('abcdefghij'))
df.shape
vlst=list('abcdefghij')
dff=df.copy()
for i in range(10):
    dff[vlst[i]]=(df[vlst[i]]-df[vlst[i]].mean())/df[vlst[i]].std()
    dff[vlst[i]]=(dff[vlst[i]]-dff[vlst[i]].min())/(dff[vlst[i]].max()-dff[vlst[i]].min())
    
dff
#65-66 Skip
#67 
#68 In df, find the second largest value of 'taste' for 'banana'
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,'rating': np.random.rand(9), 'price': np.random.randint(0, 15, 9)})
df
df.loc[df['fruit']=='banana','rating'].nlargest(2).sort_values()

#69 Compute the mean price of every fruit, while keeping the fruit as another column 
#nstead of an index.
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3, 'rating': np.random.rand(9),'price': np.random.randint(0, 15, 9)})
df
K=df.groupby('fruit')['price'].mean()
K.reset_index()

#70 Join dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’.
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3, 'weight': ['high', 'medium', 'low'] * 3,'price': np.random.randint(0, 15, 9)}) 
df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,  'kilo': ['high', 'low'] * 3,'price': np.random.randint(0, 15, 6)}) 
df1
df2

pd.merge(df1,df2,how='inner',left_on=['fruit','weight'],right_on=['pazham','kilo'], indicator=True)
help(pd.merge)

#71
#72

#73 Create two new columns in df, one of which is a lag1 (shift column a down by 1 row) of column ‘a’ 
# and the other is a lead1 (shift column b up by 1 row).

df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd' )) 

df['N1']=np.nan
df['N2']=np.nan    

df['N1']=df['a'].shift(1)
df[['N1','a']].head(10)
df['N2']=df['b'].shift(-1)
df[['N1','a','N2','b']].head(10)

#74 Get the frequency of unique values in the entire dataframe df.
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
df.nunique()
a=list(set(df['a']))
b=list(set(df['b']))
c=list(set(df['c']))
d=list(set(df['d']))
K=set(a+b+c+d)
K

a=df['a']
b=df['b']
c=df['c']
d=df['d']

J=pd.concat([a,b,c,d])
J.value_counts().sort_index()

#75 Split the string column in df to form a dataframe with 3 columns as shown
df = pd.DataFrame(["STD, City\tState", "33, Kolkata\tWest Bengal", "44, Chennai\tTamil Nadu", "40, Hyderabad\tTelengana", "80, Bangalore\tKarnataka"], columns=['row']) 
print(df)


df['STD']=df['row'].str.split(',').str.get(0)
df['CS']=df['row'].str.split(',').str.get(1)

df['City']=df['CS'].str.split("\t").str.get(0)
df['State']=df['CS'].str.split("\t").str.get(1)
df
df.drop(["CS","row"], axis=1, inplace=True)

#76

#Movie    
Movies=pd.read_csv('D:\Python\Data\movies_data.csv')
Movies.shape
Movies.columns
Movies.iloc[:,10].dtypes
Movies.iloc[:,10].nunique()
Movies['popularity'].nunique()

def VG (x,f):
    #K=print("D:/Python/Data/"+x+".pkl")
    x.to_pickle("D:\\Python\\Data\\" + f + ".pkl")
    return x.describe()

VG(Movies,"Movies")
 
def foo(**kwargs):
    for arg_name in kwargs:
        x.to_pickle("D:\\Python\\Data\\" + arg_name + ".pkl")   
   
foo(Movies_data=1)

