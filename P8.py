# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:22:53 2017

@author: 84338
"""
from functools import reduce

#连乘算法
def product(numbers):
    return reduce(lambda x,y:x*y,numbers)


if __name__=='main':
    number=''
    with open('1000_digits.txt') as f:
        for line in f:
            number+=str(line[:-1])
    
    max_product=0
    for i in range(0,986):
        temp=product([int(n) for n in number[i:i+13]])
        if temp>max_product:
            max_product=temp
    
    print(max_product)