# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:56:56 2017

@author: 84338
"""

from math import log10

# fibonacci series with cache
def fib(n):
    global _fib
    _fib=[1,1]
    
    while len(_fib)<=n:
        _fib.append(_fib[-1]+_fib[-2])
    
    return _fib[n]

def condition(i):
    if log10(fib(i))<999:
        return True
    else:
        return False

# binary search
i,j=2,2
    
while condition(i):
    j=i
    i*=2
    
while i-j>3:
    temp=(i+j)//2
    if condition(temp):
        j=temp
    else:
        i=temp

for k in range(j,i):
    if not condition(k):
        print(k+1)
        break
        
        