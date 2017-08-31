# -*- coding: utf-8 -*-

from Euler_Lib import eratosthenes

prime_sets=set(eratosthenes(1000001))

def rotations(num):
    result=[]
    num=str(num)
    for i in range(len(num)):
        num=num[-1]+num[:-1]
        result.append(int(num))
    return tuple(result)

def main():
    circular=[]
    for prime in prime_sets:
        test=rotations(prime)
        if all([rotation in prime_sets for rotation in test]):
            circular+=test
    
    circular=set(circular)
    print(len(circular))

if __name__=='__main__':
    main()