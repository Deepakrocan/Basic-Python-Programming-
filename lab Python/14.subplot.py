# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:44:36 2023

@author: MCA-05
"""


import matplotlib.pyplot as plt
import numpy as np

#Plot 1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)

#Plot 2:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()
