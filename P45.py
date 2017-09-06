# -*- coding: utf-8 -*-

from P44 import PentagonalQ
from math import sqrt


def Triangle(n):
    return n*(n+1)/2

def HexagonalQ(m):
    if (1+sqrt(1+8*m))%4==0:
        return True
    else:
        return False
    

i=286 
while i<100000:
    num=Triangle(i)
    if PentagonalQ(num) and HexagonalQ(num):
        print(num)
        break
    i+=1