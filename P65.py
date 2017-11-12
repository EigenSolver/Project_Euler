# -*- coding: utf-8 -*-

from fractions import Fraction

def euler_frac(n):
    def map_index(n):
        if (n-2)%3==1:
            return 2*((n-2)//3+1)
        else:
            return 1

    if n==1:
        return 2
    else:
        k=map_index(n)
        last=Fraction(1,k)

        while n>2:
            n-=1
            k=map_index(n)
            last=Fraction(1,Fraction(last+k))
        return Fraction(2+last)

count=0
res=euler_frac(100).numerator
for i in str(res):
    count+=int(i)
print(count)