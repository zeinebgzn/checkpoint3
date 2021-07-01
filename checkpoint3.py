#!/usr/bin/env python
# coding: utf-8

# In[1]:


# qst 1
import functools as ft
list = [2,3,6]
print(ft.reduce(lambda a,b : a*b, list))


# In[1]:


# qst 2
lis = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def Rang(x):
    return x[1]
lis.sort(key = Rang)
print(lis)


# In[3]:


# qst 3
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d = Counter(d1) + Counter(d2)
print(d)


# In[8]:


# qst 4
dic = {}
i = 1
while i<= 8:
    dic[i] = i*i
    i += 1
print(dic)


# In[9]:


# qst 5
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

def rang(x):
    return float(x[1])
list.sort(key = rang, reverse = True)
print(list)


# In[ ]:




