# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:16:43 2023

@author: MCA-05
"""


print("using tuple...")
thistuple=("apple","orange","banana")
print(thistuple)
print(len(thistuple))
print(thistuple[1])
for x in thistuple:
    print(x)
print(len(thistuple))
tuple1=("a","b","c")
tuple2=(1,2,3,4)
tuple3=tuple1+tuple2
print(tuple3)

print("Using Dictionary...")
thisdict={
    "Vehicle":"car",
    "brand":"maruthi",
    "color":"red",
    "capacity":4
    }
print(thisdict)
del thisdict["color"]
print(thisdict)