# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:35:06 2017

@author: 84338
"""
from Euler_Lib import eratosthenes
import fractions

def find_circle(string):
    for i in range(1,len(string)//2):
        if string[:i]==string[i:2*i]:
            return i
    else:
        return None

primes=eratosthenes(1000)
result=[]
for i in primes:
    string=str(decimal.Decimal(1/i)).split('.')[-1]
    result.append(find_circle(string))

print(result)

        