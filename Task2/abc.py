#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Roots of second degree polynomials
from math import *

print('This tools solves roots of polynomials of the form ax^2 + bx +c')
print('Enter coefficients a, b and c respectively')
a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if (D > 0):
    x1 = (-b + sqrt(D))/(2 * a)
    x2 = (-b - sqrt(D))/(2 * a)
    print (f'The solutions are: {x1}, {x2}')
elif (D == 0):
    x1 = -b/(2 * a)
    print(f'The solution is: {x1}')
else:
    print(f'There is no solution within the real numbers')

