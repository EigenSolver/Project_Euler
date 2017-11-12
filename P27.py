# -*- coding: utf-8 -*-
from Euler_Lib import eratosthenes
import numpy as np

test_prime=set(eratosthenes(10000))
primes=eratosthenes(1000)

def count_prime(f,limit=10000):
    count=0
    i=0
    while i<limit:
        if f(i) in test_prime:
            count+=1
        else:
            break
        i+=1
    return count


flag=0
result=0

for c in primes:
    start=int(np.sqrt(c))
    for b in np.arange(-1001,1001):
        f=lambda x: x**2+b*x+c
        n=count_prime(f)
        if n>flag:
            flag=n
            result=(b,c,b*c)
            
print(result)
        
