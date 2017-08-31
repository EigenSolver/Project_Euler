# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 02:08:01 2017

@author: 84338
"""

digits=str(2**1000)

number=0
for i in range(len(digits)):
    number+=int(digits[i])
    
print(number)