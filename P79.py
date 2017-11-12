# -*- coding: utf-8 -*-

path='p079_keylog.txt'
with open(path) as f:
    data=[]
    for line in f:
        data.append(line.strip())

#print(data)

#f=lambda x: any([x in num for num in data])
#chars=map(str,range(10))
#print(list(map(f,chars)))

def is_valid(comb,code):
    temp1=0
    temp2=0
    for i in comb:
        temp1=temp2
        temp2=code.find(i)
        if temp2-temp1<0:
            return False
    return True

def permutation(string):
    #bad implementation
    if len(string)==1:
        return string
    else:
        result=[]
        for i in range(len(string)):
            char=string[i]
            remain=string[:i]+string[i+1:]
            result+=[char+p for p in permutation(remain)]
        return result
    
possible=permutation('01236789')
for code in possible:
    if all([is_valid(comb,code) for comb in data]):
        print(code)
        break