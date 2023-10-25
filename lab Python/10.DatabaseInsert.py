# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:11:00 2023

@author: MCA-05
"""


import sqlite3
conn=sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE Company (ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL, AGE INT NOT NULL);''')
print("Table created successfully")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE) VALUES (1, 'Arun. A', 25)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE) VALUES (2, 'Babu. S', 26)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE) VALUES (3, 'Hari. D', 28)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE) VALUES (4, 'Vignesh. E', 24)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE) VALUES (5, 'Rangaraj. S', 29)")
conn.commit()
print("Records created successfully")

