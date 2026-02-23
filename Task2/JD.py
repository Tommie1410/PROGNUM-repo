#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Julian date
print('This is the Julian date calcualtor')
print('Enter the year')
Y = int(input())
print('Enter the month')
M = int(input())
print("Enter the day")
D = float(input())

JD = 367*Y-7*((Y+(M+9)/12)/4)-3*((Y+(M-9)/7)/100+1)/4+(275*M)/9+D+1721029-0.5

print('The Julian date is:', JD)


# In[ ]:




