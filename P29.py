## -*- coding: utf-8 -*-
#"""
#Created on Fri Jul 28 14:11:35 2017
#
#@author: 84338
#"""
#from math import log
#
#class power(object):
#    def __init__(self,n,p):
#        self.n=n
#        self.p=p
#    
#    def __eq__(self,other):
#        n,p=(other.n,other.p)
#        if (n,p)==(self.n,self.p):
#            return True
#        elif n>self.n:
#            ratio=log(n,self.n)
#            if ratio%1==0:
#                if ratio*p==self.p:
#                    return True
#            else:
#                return False
#
#        elif n<self.n:
#            ratio=log(self.n,n)
#            if ratio%1==0:
#                if ratio*self.p==p:
#                    return True
#            else:
#                return False
#        else:
#            return False
#
#count=[]
#for i in range(2,101):
#    for j in range(2,101):
#        if count==[]:
#            count.append(power(i,j))
#        elif not any([power(i,j)==num for num in count]):
#            count.append(power(i,j))
#    
#print(len(count))

import numpy as np
count=[]
for i in range(2,101):
    for j in range(2,101):
        count.append(i**j)
print(len(set(count)))