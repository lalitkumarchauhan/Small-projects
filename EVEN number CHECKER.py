#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Program to check whether the entered number is am even number or non-even number

# getting the input from the user
num = input('Please enter the number that is to checked: ')
num = float(num) # converting the datatype of the number as the input was in string format
print('Thank you for entering the number, We have converted your input to an floating point number for simplification')

if num%2 == 0:
    print(str(num) + ' is an Even number')
elif num%2 != 0:
    print (str(num) + ' is not an Even number')

