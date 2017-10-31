# -*- coding: utf-8 -*-

d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

with open("p089_roman.txt") as f:
    data=[]
    for line in f:
        data.append(line.strip())

def find_sum(string,dictionary=d):
    count=0
    for char in string:
        count+=dictionary[char]
    for i in range(1,len(string)):
        if d[string[i]]>d[string[i-1]]:
            count-=2*dictionary[string[i-1]]
    return count

def eff_num(num,d={'0':0,'1':1,'2':2,'3':3,'4':2,'5':1,'6':2,'7':3,'8':4,'9':2}):
    count=0
    count+=num//1000
    num=num%1000
    for i in str(num):
        count+=d[i]
    return count

sum_all=0
mini=[]
for s in data:
    sum_all+=len(s)
    sum_all-=eff_num(find_sum(s))
print(sum_all)
    