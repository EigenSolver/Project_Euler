# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:57:24 2017

@author: 84338
"""
# 遍历优化
from P8 import product


def main():
    for a in range(1,999):
        for b in range(1,1000-a):
            c=1000-a-b
            edge=[a,b,c]
            edge.sort()
            if (edge[0]**2+edge[1]**2==edge[2]**2):
                print(edge)
                print(product(edge))
                return 0

if __name__=='main':
    main()