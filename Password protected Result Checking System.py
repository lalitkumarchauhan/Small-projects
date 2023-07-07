#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Password protected result checking system:

#Taking input from user:

password = input("Kindly your password please: ")
score = input("Now, please enter your score: ")

cutoff= 30 #hardcoding the cutoff score
real_password = 123 # the password is also hardcoded

#Converting data type of score (i.e. string) to integer:
password = int(password)
score = int(score)

#nested if else statements
if password == real_password: # password comparison
    if score>=0:
        if score<cutoff:
            print("Sorry, you have failed in the exam.")
        else:
            print("Congratulations! You have passed the exam.")
    else:
        print('Please enter the valid score :(')
else:
    print('Incorrect Password. Access Denied')


# In[ ]:




