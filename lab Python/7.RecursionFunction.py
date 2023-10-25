# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:09:44 2023

@author: MCA-05
"""


def tri_recursion(k):
  if(k > 0):  
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) 

