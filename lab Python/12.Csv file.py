# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:21:48 2023

@author: MCA-05
"""


import pandas as pd
sdata=pd.read_csv('student.csv')
print(sdata)
print(sdata.loc[2,:])