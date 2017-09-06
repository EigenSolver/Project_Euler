# -*- coding: utf-8 -*-

from P3 import gcd
from collections import Counter

def triple_numbers(m,n):
    '''
    Euclid's formula to produce a Pythagorean triple with two parameters m,n 
    m,n must be coprime
    '''
    return (m**2-n**2,m**2+n**2,2*m*n)


triples=[]

for m in range(1,32):
    for n in range(1,m-1):
        if gcd(m,n)==1:
            triples.append(triple_numbers(m,n))

triples=set(triples)

sums=[]

for tri in triples:
    if sum(tri)<1000:
       sums.append(sum(tri)) 
        
print(Counter(sums).most_common()[0])


        
    