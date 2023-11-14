# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 04:30:40 2023

@author: tejas
"""

L = [1,2,4,8,16,32,64]
X = 5

i= 0
while i< len(L):
    if 2**X == L[i]:
        print('found at index',i)
        break
    i+=1

else:
    print('not found')