# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 02:09:54 2023

@author: tejas
"""

import time
from scipy.special import factorial

def calculate_factorial(n):
    start_time = time.time()

    result = factorial(n)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Factorial of {n} is: {result}")
    print(f"Time taken to calculate factorial: {elapsed_time} seconds")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a non-negative integer: "))
        if user_input < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            calculate_factorial(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
