# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 00:09:18 2017

@author: 84338
"""
import numpy as np
from Euler_Lib import find_factors,sum_factors,eratosthenes

def abundantQ(num):
    if sum_factors(num,__prime)>num:
        return True
    else:
        return False

'''
__prime=eratosthenes(28124)

is_abundant=np.zeros(28124)
nums=np.arange(28124)

i=1
while i<28124:
    is_abundant[i]=1 if abundantQ(i) else 0 
    i+=1
    if i%1000==0:
        print(i,"finished!")

abundants=nums[is_abundant==1]

isnot_sum=np.ones(28124)

for i in range(len(abundants)):
    for j in range(i+1):
        sum_=abundants[i]+abundants[j]
        if sum_<28124:
            isnot_sum[sum_]=0

print(nums[isnot_sum==1].sum())
'''


