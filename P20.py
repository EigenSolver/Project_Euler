# -*- coding: utf-8 -*-

from P15 import factorial

count=0
for char in str(factorial(100)):
    count+=int(char)
    
print(count)