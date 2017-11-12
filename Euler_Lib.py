# -*- coding: utf-8 -*-

import numpy as np
from P3 import prime_factorization,gcd
#from P4 import palindromeQ
#from P5 import lcm
#from P7 import eratosthenes
#from P8 import product
#from P12 import triangle_number,find_factors,num_of_factors
#from P15 import factorial,step_factorial,combination
#from P17 import gimmeThemWords
#from P21 import sum_factors
#from P23 import abundantQ
#from P28 import sprial_number
#from P37 import trunctableQ
#from P38 import pandigitalQ
#from P45 import PentagonalQ,HexagonalQ


def permutations(string):
    if len(string)<2:
        return string

    result=[]
    for i in range(len(string)):
        remain=string[:i]+string[i+1:]
        letter=string[i]
        result+=list(map(lambda x: letter+x,permutations(remain)))
    return result

def eratosthenes(end, start=2, return_boolean=False):
    """
    Finds all primes < `end`.

    :param end: An integer. The upper limit of the range to look for primes.
    :param start: An integer. The start of the range to look for primes.
    :param return_boolean: A boolean. Represents the type of return type.
    :rtype: Depending on `return_boolean` either returns boolean and primes or
            just the primes.
    """
    primes = np.arange(end+1)
    if end < start or end < 2:
        return []
    is_prime = np.ones(end+1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, end + 1):
        if not is_prime[i]:
            continue
        j = i * i
        while j <= end:
            is_prime[j] = 0
            j += i
    if return_boolean:
        return primes[is_prime==1], is_prime
    return primes[is_prime==1]
