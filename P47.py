# -*- coding: utf-8 -*-

from Euler_Lib import eratosthenes
import numpy as np
from math import sqrt 


limit=200000
start=0
end=limit

CONST=4
result=0

__primes,is_prime=eratosthenes(limit,return_boolean=True)

def DPF(number,primes):
    if number in primes:
        return 1
    result=0
    if primes is None:
        primes=eratosthenes(int(sqrt(number)+1))
    for p in primes:
        if p>number:
            break
        if number%p==0:
            result+=1
            while number%p==0:
                number//=p
    return result

domain=np.arange(start,end)
dist_fac=np.zeros(len(domain))

for i in range(len(domain)):
    dist_fac[i]=DPF(domain[i],__primes)
    if i%3000==0:
        print('{0}/{1} has finished!'.format(i,len(domain)))
        

print('\n factors calculation finished!')

for i in range(len(domain)-CONST):
    if np.sum(dist_fac[i:i+CONST]==CONST)==CONST:
        result=domain[i]
        print(result)


