# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import pyodbc
import pandas as pd

connection = pyodbc.connect('Driver={Oracle in OraClient11g_home1};DBQ=pacfin;Uid=uid;Pwd=pw')

#test the connection
cursor = connection.cursor()

#Example command to print the unique values of the field 'pacfin_group_gear_code' 
SQLCommand = ("SELECT distinct pacfin_group_gear_code FROM pacfin_marts.comprehensive_ft")
cursor.execute(SQLCommand)
print cursor.fetchall()

> [('HKL', ), ('TWL', ), ('TLS', ), ('POT', ), ('TWS', ), ('MSC', ), ('NET', )]

#try to get results into pandas data frame...here I'm going to do a count of the field 'FTID' by year
sql = ("SELECT pacfin_year, count(FTID) FROM pacfin_marts.comprehensive_ft group by pacfin_year")
cnn = pyodbc.connect('Driver={Oracle in OraClient11g_home1};DBQ=pacfin;Uid=amamula;Pwd=mam2pac$')
data = pd.read_sql(sql, cnn)


############### My code
cnn = pyodbc.connect('Driver={Oracle in Ora12c_h64};DBQ=ddprd00_all.vanguard.com;Uid=upal;Pwd=Shanxilaocha001')

c=cnn.cursor() 

sql = ("SELECT * from UWEN.PRIMARY_REPORTEE_YYYYMM fetch first 10 rows only")
c.execute(sql)

#produce pandas data
Mydata=pd.read_sql(sql, cnn)


#db2
cnn = pyodbc.connect('Driver={IBM DB2 ODBC DRIVER - DB2COPY1};DBALIAS=DP0R; Uid=upal;Pwd=Shanxilaocha001')

c=cnn.cursor() 

sql = ("SELECT * from AVGI00.PRIMARY_REPORTEE_YYYYMM fetch first 10 rows only")
c.execute(sql)


#produce pandas data
Mydata=pd.read_sql(sql, cnn)

