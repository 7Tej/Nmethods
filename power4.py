# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 05:03:07 2023

@author: tejas
"""
from timeit import *
start = default_timer()
L = []
X = 5


for i in range(7):
    L.append(2**i)
print(L)

if (2**X in L):
    print('at index',L.index(2**X))
    
else:
    print('not found')
print("Time taken (in sec) =",default_timer()-start)