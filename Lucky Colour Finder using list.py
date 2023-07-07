#!/usr/bin/env python
# coding: utf-8

# In[2]:


#to find a colour based upon the number provided by the user as input (between 1 and 10)

colour_list = ["Brown", "Blue", "Red", "Orange", "Yellow", "Green", "Black", "White", "Violet", "Magenta", "Pink"]
#https://onlymyenglish.com/colors-name-english/

#Getting the input from the user
num = input("Enter any integer between 0 to 10: ")

#changing the datatype of the user input as the input is in string format
index = int(num)

lucky_colour = colour_list[index]
print('Your lucky colour is ',lucky_colour  )

