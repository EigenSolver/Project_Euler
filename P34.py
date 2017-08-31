# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:44:39 2017

@author: 84338
"""

import numpy as np
from Euler_Lib import factorial

def brute_force():
    bounds=2540160
    
    result=[]
    
    def func(x):
        return factorial(x)
    
    for number in range(bounds):
        count=0
        for char in str(number):
            count+=func(int(char))
            if count>number:
                break
        if count==number:
            result.append(number)
            
    print(sum(result)-3)

def main():
    numbers=np.arange(10)
    np.apply_over_axes(numbers,factorial)
    