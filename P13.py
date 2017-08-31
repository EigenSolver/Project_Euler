# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 22:41:29 2017

@author: 84338
"""

numbers=[]

with open('50_digits.txt') as f:
    for line in f:
        numbers.append(int(line[:-1]))
        
print(str(sum(numbers))[:10])
