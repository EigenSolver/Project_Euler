# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 01:29:51 2017

@author: 84338
"""

'''
设P为集合S[range(10)]的全排列
P中排列p由10个数字组成
设该排列p的字典序号为n
p[i]为p中第i个元素
n=Sum[p[i]*factorial(10-i)]
则p可由如下算法确定
'''
from Euler_Lib import factorial

count=0
avaiable=list(range(10))
    
def find_next():
    global avaiable
    global count
    global temp
    temp=0
    card=factorial(len(avaiable)-1)
    while count<1000000:
        count+=card
        temp+=1
    count-=card
    nex=avaiable[temp-1]
    avaiable.remove(nex)
    return nex

result=''
while avaiable!=[]:
    result+=str(find_next())

print(result)