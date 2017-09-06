# -*- coding: utf-8 -*-

def permutations(string):
    if len(string)<2:
        return string

    result=[]
    for i in range(len(string)):
        remain=string[:i]+string[i+1:]
        letter=string[i]
        result+=list(map(lambda x: letter+x,permutations(remain)))
    return result

def sub_div_test(string):
    primes=[2, 3, 5, 7, 11, 13, 17]
    
    if all([int(string[i+1:i+4])%primes[i]==0 for i in range(7)]):
        return True
    else:
        return False
        
strings=permutations('0123456789')

valid=[]

for string in strings:
    if sub_div_test(string):
        valid.append(string)
        
print(sum(list(map(int,valid))))