# -*- coding: utf-8 -*-

import math

def digits_of_comb(n,r):
    count=0
    for i in range(r):
        count+=math.log10(n-i)
        count-=math.log10(i+1)
    return count

count=0
for n in range(23,101):
    for r in range(2,n-1):
        if digits_of_comb(n,r)>6:
            count+=1

print(count)