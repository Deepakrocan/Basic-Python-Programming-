# List Mare tha Duplicate Add Panu Tuples

# but You cannot modify the tuple... we connot add and remove in tuple

a=(1,2,3,4,5)
a[0]=10    # tuple object connot assignment in data type's
print(a)

#But You can modify the casting in the tuple

a=(1,2,3,4,5)
b=list(a)
b.pop() # you can use b opction wha twe can do in tuple's
print(b)

# ---------------------------------------------------------------


# Set {}  =>     
# Do not allow Duplicate value will be remove
# we cannot modify the set bur you can (add and remove)  
# You cannot update the set 

a=(1,2,3,4,5,1)
print(a)
# set is a unorder the list 
a.add(10)



# pop meaning is  delete 


#  - - - - -  - - - - - - - - - - -

# Dictionary {} => 


# DO not allow Duplicate value  but Duplicate will overwrite existing value  modify
#del a["age"]

a={
    "name":"Deepak",
    "Age":1
  }
print(a.keys())