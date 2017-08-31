# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:43:48 2017

@author: 84338
"""

def sprial_number(n):
    result=[1]
    for i in range(1,(n-1)//2+1):
        width=2*i
        for j in range(4):
            result.append(result[-1]+width)
    return result
