#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to calculate Profit / Loss by asking Cost and selling prices:

#Taking input from user:
cost_price = input("Enter the price at which you bought the thing: ")
selling_price = input("Enter the price at which you sold the object: ")

#Changing the data type of input from string to integer:
cost_price = int(cost_price)
selling_price = int(selling_price)

#Defining conditions using if elif else:

if cost_price<selling_price:
    profit = selling_price - cost_price
    profit = str(profit)
    print("You had a profit of: Rs." + profit)
elif cost_price>selling_price:
    loss = cost_price - selling_price
    loss = str(loss)
    print("You had a loss of: Rs." + loss)
else:
    print("You neither had profit nor loss.")


# In[ ]:




