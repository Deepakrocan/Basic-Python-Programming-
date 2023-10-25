# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:11:04 2023

@author: MCA-05
"""


import sqlite3
conn=sqlite3.connect('test.db')
print("Opened database successfully")

rs=conn.cursor()

rs.execute("SELECT ID, NAME, AGE FROM COMPANY")
records=rs.fetchall()
print("Total records are: ", len(records))
print("Printing Each Row")
for row in records:
    print("ID= ", row[0])
    print("NAME= ", row[1])
    print("AGE= ", row[2], "\n")

rs.close()
print("Date viewed successfully")

