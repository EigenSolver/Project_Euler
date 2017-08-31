# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 01:44:27 2017

@author: 84338
"""
from P7 import eratosthenes
from math import sqrt

#最大公因数
def gcd(m,n):
    diff=1
    if m<n:
        m,n=n,m
    while diff!=0:
        diff=m-n
        m,n=(n,diff) if diff<n else (diff,n)
    return m

#print(gcd(39,13))

#质数生成算法
def prime(end,start=2):
   global __prime
   try:
     __prime
   except NameError:
     __prime=[2]
   for i in range(__prime[-1],end+1):
       if all([i%j!=0 for j in __prime]):
           __prime.append(i)
   return __prime

#质因子分解算法
def prime_factorization(number, primes=None):
    if primes is None:
        primes=eratosthenes(int(sqrt(number)+1))
    prime_factors=[]
    for p in primes:
        n=0
        while number%p==0:
            number/=p
            n+=1
        prime_factors.append((p,n)) if n!=0 else None
    return prime_factors

'''
if __name__=='__main__':
    print(prime_factorization(600851475143))
'''
    