#!/usr/bin/env python
# coding: utf-8

# In[35]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
moon = masses[-2]

masses_new = []
for i in range(len(masses)):
    if (masses[i] >= moon):
        masses_new.append(masses[i])
print(masses_new)

print(masses[slice(-5,len(masses),1)],'\n')

avg_mass = (sum(masses_new)/len(masses_new))
print(avg_mass)


# In[ ]:




