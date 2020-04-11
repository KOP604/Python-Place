
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# RUN selection F9

# # SF Salaries Exercise 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.
# ** Import pandas as pd.**

# In[4]:

from numpy.random import randn
randn(5,4)


# In[1]:

import pandas as pd

# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:

sal=pd.read_csv("D://Python/Salaries.csv")
sal.head()

sal.info()


# **What is the average BasePay ?**

# In[18]:

sal["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[19]:

sal["OvertimePay"].max()


# In[11]:



# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[28]:

sal.JobTitle[sal.EmployeeName=="JOSEPH DRISCOLL"]


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[29]:

sal.TotalPay[sal.EmployeeName=="JOSEPH DRISCOLL"]


# ** What is the name of highest paid person (including benefits)?**

# In[36]:

Tpay=sal["TotalPay"].max()
sal.EmployeeName[sal.TotalPay==Tpay]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[4]:

Bpay=sal["TotalPay"].min()
sal[sal.TotalPay==Bpay]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[6]:

sal.groupby(['Year'])['BasePay'].mean()


# ** How many unique job titles are there? **

# In[10]:

len(sal["JobTitle"].unique())


# ** What are the top 5 most common jobs? **

# In[22]:

TS=sal.groupby(["JobTitle"]).count()
TS.sort_values(by=["Id"],ascending=False).head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[24]:

TS=sal.groupby(["JobTitle"]).count()
TS.sort_values(by=["Id"]).head()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[33]:

len(sal[sal["JobTitle"].str.contains('Chief')])
#df[df['model'].str.contains('ac')]


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[46]:

#c=sal[["JobTitle","BasePay"]]
#c.corr()
sal[["JobTitle","BasePay"]].corr()


# In[23]:




# # Great Job!
