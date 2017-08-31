# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:29:08 2017

@author: 84338
"""


from functools import partial
from math import log10

def get_last_digits(number,n):
    return int(str(number)[-n:])

last_ten=partial(get_last_digits,n=10)

result=[]
for n in range(1,1001):
    i=0
    count=1
    while i<n:
        count*=n
        i+=1
        if len(str(count))>=10:
            count=last_ten(count)
    result.append(count)

print(last_ten(sum(result)))