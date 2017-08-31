# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:32:32 2017

@author: 84338
"""
#字符串处理和列表计算 python使用了numpy
from P8 import product
import numpy as np

def search_adjecent(square, length=4):
    numbers=np.array(square)
    square.reverse()
    reverse_numbers=np.array(square)
    def adj(i,length):
        return [i+j for j in range(length)]
    
    maxs=[]
    for i in range(numbers.shape[0]-length):
        hor=numbers[:,i:i+length]
        ver=numbers.T[:,i:i+length]
        maxs.append(max(product(hor.T).max(),product(ver.T).max()))
        for j in range(numbers.shape[0]-length):
            maxs.append(product([reverse_numbers[x,y] for x,y in zip(adj(i,length), adj(j,length))]))
            maxs.append(product([numbers[x,y] for x,y in zip(adj(i,length), adj(j,length))]))
    return max(maxs)
    
if __name__=='__main__':
    square=[]
    with open('square.txt') as f:
        for line in f:
            square.append(list(map(int,line[:-1].split(' '))))

    print(search_adjecent(square))
    