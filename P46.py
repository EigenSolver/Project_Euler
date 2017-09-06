# -*- coding: utf-8 -*-

from P7 import eratosthenes
import numpy as np

length=10000

__primes=eratosthenes(length)

prime_test=set(__primes)

def GoldbachTest(Odd):
    Odd_primes=[]
    for i in __primes:
        if i%2!=0 and i<Odd:
            Odd_primes.append(i)
    Odd_primes=np.array(Odd_primes)
    if any(np.sqrt((Odd-Odd_primes)/2)%1==0):
        return True
    else:
        return False
    
n=9

while n<length:
    n=n+2
    if n in prime_test:
        continue
    if not GoldbachTest(n):
        print(n)
        break
