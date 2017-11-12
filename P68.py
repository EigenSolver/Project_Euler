# -*- coding: utf-8 -*-

from itertools import combinations
import numpy as np

def ring_sum(string,n=5,m=2):
    count=[]
    for i in range(n):
        sum_=string[i]
        for j in range(m):
            if i+j+n!=10:
                sum_+=string[i+j+n]
            else:
                sum_+=string[5]
        count.append(sum_)
    return count

def ring_recons(string,n=5,m=2):
    count=''
    for i in range(n):
        sum_=str(string[i])
        for j in range(m):
            if i+j+n!=10:
                sum_+=str(string[i+j+n])
            else:
                sum_+=str(string[5])
        count+=sum_
    return count

def form_cycle(comb):
    X=np.array(comb)
    A=np.array(((-1,1,-1,1,-1),(-1,-1,1,-1,1),(1,-1,-1,1,-1),(-1,1,-1,-1,1),(1,-1,1,-1,-1)))
    new=8+1/2*np.dot(A,X)
    return new

result=[]
possible=(1,2,3,4,5,6,7,8,9,10)
for comb in combinations(possible,5):
    X_=np.array(comb)
    X_remain=form_cycle(comb)
    if sum(X_remain%1)==0:
        X=np.hstack([X_remain,X_]).astype(int)
        if all([i in X for i in possible]):
            result.append((X_,X_remain))

#print(ring_sum(result[0]))
#print(ring_recons(result[0]))