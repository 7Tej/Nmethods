# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 05:03:07 2023

@author: tejas
"""
from timeit import *
start = default_timer()
L = []
X = 5
y= 2**X

for i in range(7):
    L.append(2**i)
print(L)

if (y in L):
    print('at index',L.index(y))
    
else:
    print('not found')
print("Time taken (in sec) =",default_timer()-start)