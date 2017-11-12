# -*- coding: utf-8 -*-

def digit_sum(n):
    n=str(n)
    res=0
    for i in n:
        res+=int(i)
    return res


max_sum=0
for a in range(1,100):
    if a%10==0:
        continue
    for b in range(1,100):
        dig_sum=digit_sum(a**b)
        if dig_sum>max_sum:
            max_sum=dig_sum

print(max_sum)