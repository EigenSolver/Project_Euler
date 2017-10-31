# -*- coding: utf-8 -*-

from Euler_Lib import eratosthenes
import numpy as np

limit=150000
__primes=eratosthenes(limit)
print('num of primes calculation finished!')

@np.vectorize
def DPF(num):
    '''
    find the number of distinct prime factors given a integer num
    '''
    result=0
    for p in __primes:
        if p>=num:
            break
        if num%p==0:
            result+=1
            while num%p==0:
                num//=p
    return result

domain=np.arange(limit)
num_of_factors=np.zeros(limit)

print('num of factors calculation finished!')

CONST=4
for i in range(len(domain)):
    group=[num_of_factors[i+j] for j in range(CONST)]
    if all([num==CONST for num in group]):
        print(group)
        break

