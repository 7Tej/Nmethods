# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:38:50 2023

@author: tejas
"""

#Fibonacci Numbers

def fib(n):
    if n==1 or n==2:
        return 1
    for i in range(3,n+1):
        return fib(n-2)+fib(n-1)

for j in range(1,11):
    print (fib(j))