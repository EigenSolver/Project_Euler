# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:53:48 2017

@author: 84338
"""
import numpy as np
from Euler_Lib import find_factors,eratosthenes

def sum_factors(n,__prime):
    return sum(find_factors(n,__prime)[:-1])

'''
__prime=eratosthenes(100001)

is_amicable=np.array([False for i in range(100001)])
div_sum=np.array([0 for i in range(100001)])


    for i in range(2,10001):
        if div_sum[i]==0:
            j=sum_factors(i)
            
            div_sum[i]=j

            if j<=10000 and j!=i:
                swap=sum_factors(j)

                div_sum[j]=swap
                if swap==i:
                    is_amicable[i],is_amicable[j]=(True,True)
        if i%1000==0:
            print(i,' has finished!')

    print(div_sum[is_amicable].sum())
'''
   