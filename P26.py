# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:35:06 2017

@author: 84338
"""

import numpy as np

@np.vectorize
def len_of_circle(n):
    limit=1000
    remain=10**(len(str(n)))%n
    remains=[remain]
    time=0

    while time<limit:
        if remain==0:
            return 0
        remain*=10
        while remain<n:
            remain*=10
            remains.append(-1)
        remain=remain%n
        l=len(remains)
        for i in range(l):
            if remains[i]!=-1 and remains[i]==remain:
                return l-i
        remains.append(remain)
        time+=1
    return -1

domain=np.arange(1,1000)
result=len_of_circle(domain)
if (-1) in result:
    print(result==-1)
else:
    print(result.argmax()+1)


