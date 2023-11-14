# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 02:56:18 2023

@author: tejas
"""
L = [1,2,4,8,16,32,64]
X = 5

for m in L:
    if 2**X == m:
        print('found at index',L.index(m))
        break
else:
    print('not found')

