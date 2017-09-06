# -*- coding: utf-8 -*-

from Euler_Lib import prime_factorization,eratosthenes
import numpy as np



def DPF(n):
    return len(prime_factorization(n,__primes))
    

__primes=eratosthenes(100000)

start=647
end=1000000

CONST=4
result=0


domain=np.arange(start,end)
dist_fac=np.zeros(len(domain))
for i in range(len(domain)):
    dist_fac[i]=DPF(domain[i])
    print(i)
    if i%10000==0:
        print('{0}/{1} has finished!'.format(i,len(domain)))
        

print('factors calculation finished!')

for i in range(len(domain)-CONST):
    group=[start+i for i in range(CONST)]
    if all([dist_fac[i]==CONST for i in group]):
        result=domain[i]
        break
    start+=1


