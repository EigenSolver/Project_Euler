# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:32:04 2017

@author: 84338
"""

from Euler_Lib import palindromeQ

both=[]
for i in range(1000000):
    if palindromeQ(bin(i)[2:]) and palindromeQ(i):
        both.append(i)
        
print(sum(both))

