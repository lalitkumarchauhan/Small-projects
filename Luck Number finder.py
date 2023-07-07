#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Program to find the Lucky number 
by using a logic (Length of name + length of favourite color strings)
The name and favourite colour will be asked from the user
"""
#Welcome prompt to the user
print('Welcome to Lucky number calculator')


# input clause to ask the user to input the name and favourite colour
name = input("Enter your name please: ")
colour_fav = input("Type in your favourite colour: ")

#finding the length of the two strings using inbuilt len funtion
len_name = len(name)
len_colour_fav = len(colour_fav)


# adding the number length of two strings to calculate the lucky number by pre-defined logic
lucky_number = len_name + len_colour_fav 

print('\n\nHey! ' + name)
print('Your lucky number is ' + str(lucky_number)) # converting the integer to string by typecasting lucky_number
print('\nThank you for using the Lucky number calculator!!! Stay healthy!') # thank you prompt


# In[ ]:




