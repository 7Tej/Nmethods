# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:00:31 2023

@author: tejas
"""
print((lambda n, fib=[0, 1]: fib + [fib.append(fib[-2] + fib[-1]) or fib[-1] for _ in range(8)])(10))




