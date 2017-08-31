# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:05:06 2017

@author: 84338
"""
numbers=[]
for i in range(100,1000):
    for j in range(100,1000):
        numbers.append(i*j)

#回文判定
def palindromeQ(n):
    n=str(n)
    if all([n[i]==n[-i-1] for i in range(0,len(n)//2)]):
        return True
    else:
        return False
    
if __name__=='__main__':
    print(max(filter(palindromeQ,numbers)))