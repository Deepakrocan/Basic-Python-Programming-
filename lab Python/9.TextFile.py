# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:31:30 2023

@author: MCA-05
"""


file1 = open("myfile.txt","w") 
L = ["Hello jaganathar temple of odisa"]  
file1.write("Hello \n") 
file1.writelines(L) 
file1.close()
file1 = open("myfile.txt","r")
file1.seek(0)  
print ("Output of Readline function is ")
print (file1.readline()) 
print
file1.seek(0) 
print ("Output of Readlines function is ")
print (file1.readlines() )
print
file1.close() 
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()
f=open("binfile.bin","rb")
num=list(f.read())
print (num)
f.close()
