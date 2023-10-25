# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:50:09 2023

@author: MCA-05
"""


def swap(a,b):
    temp=a
    a=b
    b=temp
    print("after swap:",a,b)
    return
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print("before swap:",n1,n2)
swap(n1,n2)
