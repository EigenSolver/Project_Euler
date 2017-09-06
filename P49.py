# -*- coding: utf-8 -*-

from Euler_Lib import permutations,eratosthenes

primes=eratosthenes(10000)

primes=list(filter(lambda x: len(x)>3,list(map(str,primes))))
primes_test=set(primes)

def permutationQ(string1,string2):
    if string1 in permutations(string2):
        return True
    else:
        return False

result=[]

for prime in primes:
#    incre=3330
    increa=list(map(str,(int(prime)+3330,int(prime)+6660)))

    if all([x in primes for x in increa]):
        if all([x in permutations(prime) for x in increa]):
            concat=''
            for i in increa:
                concat+=i
            result.append(prime+concat)

#    permu=permutations(prime)
#    count_in=0
#    for i in permu:
#        if i in primes:
#            count_in+=1
#    if count_in==3:
#        result.append(prime)
        
#    if sum([(permu in primes) for permu in permutations(prime)])==3:
#        result.append(prime)

print(set(result))