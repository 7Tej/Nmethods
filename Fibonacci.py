# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:00:50 2023

@author: tejas
"""
#Fibonacci Numbers
n= int(input('order of the fibonacci number'))
def fib(n):
    if n==1 or n==2:
        return 1
    for i in range(3,n+1):
        return fib(n-2)+fib(n-1)

for j in range(1,n+1):
    print(fib(j))