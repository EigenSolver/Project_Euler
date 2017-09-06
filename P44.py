# -*- coding: utf-8 -*-

from math import sqrt

def Pentagonal(n):
    return n*(3*n-1)//2

def PentagonalQ(n):
    if (1+sqrt(1+24*n))%6==0:
        return True
    else:
        return False

def search(length):
    Pentagonals=tuple([Pentagonal(n) for n in range(1,1+length)])
    Pentagonals_test=set(Pentagonals)
    for i in range(length):
        for j in range(i+1,length):
            if Pentagonals[i]+Pentagonals[j] in Pentagonals_test:
                if Pentagonals[j]-Pentagonals[i] in Pentagonals_test:
                    return (Pentagonals[j],Pentagonals[i],Pentagonals[j]-Pentagonals[i])

#print(search(3000))
        