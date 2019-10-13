import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
def test():
    x = 2+2
    return x

print(test())

df = pd.read_csv('C:\\Users\\Sandip\\Desktop\\test_data\\india-trade-data\\2018-2010_export.csv')

first_5 = df.head()
first_5 = df.describe()
print(first_5)

connection = sqlite3.connect("myTable.db")
crsr = connection.cursor()
#crsr.execute("create table emp ( id number)")
crsr.execute("select * from emp")
ans= crsr.fetchall()
for i in ans:
    print(i)

