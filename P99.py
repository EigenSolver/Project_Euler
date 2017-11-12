# -*- coding: utf-8 -*-

from numpy import log

def process(string):
    return tuple(map(int,string.strip().split(',')))

with open('p099_base_exp.txt') as f:
    data=f.readlines()

data=list(map(process,data))


max_num=0
line_num=1

for i in range(len(data)):
    base, exponent=data[i]
    num=exponent*log(base)
    if num>max_num:
        max_num=num
        line_num=i+1
    
print(line_num)