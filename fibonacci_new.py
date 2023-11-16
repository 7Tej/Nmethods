# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:45:21 2023

@author: tejas
"""
#fibonacci sequence
def fibonacci(n):
    fib=[0,1]
    
    while len(fib)<n:
        fib.append(fib[-1]+fib[-2])
        
    return fib[:n]


    
    