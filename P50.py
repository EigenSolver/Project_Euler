# -*- coding: utf-8 -*-

from Euler_Lib import eratosthenes

primes=eratosthenes(1000000)
primes_test=set(primes)

position=0
limit=len(primes)
max_length=2
result=0


#for i in range(len(primes)):
#    length=2
#    test=0
#    
#    while test<primes[-1]:
#        end=i+length
#        if end>limit:
#            break   
#        test=sum(primes[i:end])
#        if test in primes_test:
#            if length>max_length:
#                max_length=length
#                result=test
#        length+=1
        
while position<limit:    
    length=2
    test=0
    while test<primes[-1]:
        end=position+length
        if end>=limit:
            break
        test=sum(primes[position:end])
        
        if test in primes_test:
            if length>max_length:
                max_length=length
                result=test
        length+=1

    position+=1

print(result)