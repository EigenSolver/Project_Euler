# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 00:25:06 2017

@author: 84338
"""

import numpy as np

numbers=[]

filename='p067_triangle.txt'
#filename='digit_tree.txt'

with open() as f:
    for line in f:
        numbers.append(list(map(int,line[:-1].split(' '))))

numbers=np.array(numbers)

def cal_path(numbers):
    def cal_layer(numbers,n,func=max):
        this=numbers[n]
        nex=numbers[n+1]
        for i in range(len(this)):
            this[i]+=func(nex[i],nex[i+1])

    n=len(numbers)-2 #num_of_layers
    while n>=0:
        cal_layer(numbers,n)
        n-=1
    return numbers[0][0]

print(cal_path(numbers))
