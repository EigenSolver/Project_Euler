# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:04:33 2017

@author: 84338
"""
import numpy as np

bounds=354295

'''
9^5 *6 = 354294 
for any number that have more than 6 digits,
the sum of its digits fifth will be less than itself
'''
result=[]

def func(x):
    return x**5

for number in range(bounds):
    count=0
    for char in str(number):
        count+=func(int(char))
        if count>number:
            break
    if count==number:
        result.append(number)
        
        
            
        