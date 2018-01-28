# -*- coding: utf-8 -*-
import numpy as np
from P3 import prime_factorization, gcd
from P4 import palindromeQ
from P5 import lcm
import random
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
#from P52 import permuteQ
#from P55 import lychrelQ,reverse_str


def combinationN(m, n):
    '''
    number of combination
    choose n from m 
    '''
    result = 1
    for i in range(n):
        result *= (m - i)
    for i in range(n):
        result /= (i + 1)
    return result


def combinations(string, n):
    result = []
    m = len(string)
    if m - n < n:
        n = m - n

    if n < 0:
        return None
    elif n == 0:
        return string
    elif n == 1:
        return [char for char in string]
    else:
        for i in range(len(string)):
            remain = string[:i] + string[i + 1:]
            letter = string[i]
            result += list(map(lambda x: letter + x,
                               combinations(remain, n - 1)))
        return set(result)


def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count


def permutations(string):
    if len(string) < 2:
        return string

    result = []
    for i in range(len(string)):
        remain = string[:i] + string[i + 1:]
        letter = string[i]
        result += list(map(lambda x: letter + x, permutations(remain)))
    return result


def eratosthenes(end, start=2, return_boolean=False):
    """
    Finds all primes < `end`.
    accelerated with numpy

    :param end: An integer. The upper limit of the range to look for primes.
    :param start: An integer. The start of the range to look for primes.
    :param return_boolean: A boolean. Represents the type of return type.
    :rtype: Depending on `return_boolean` either returns boolean and primes or
            just the primes.
    """
    primes = np.arange(end + 1)
    if end < start or end < 2:
        return []
    is_prime = np.ones(end + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, end + 1):
        if not is_prime[i]:
            continue
        j = i * i
        while j <= end:
            is_prime[j] = 0
            j += i
    if return_boolean:
        return primes[is_prime == 1], is_prime
    return primes[is_prime == 1]


def decompose(n):
    exponentOfTwo = 0

    while n % 2 == 0:
        n = n / 2
        exponentOfTwo += 1

    return exponentOfTwo, n


def isWitness(possibleWitness, p, exponent, remainder):

    possibleWitness = pow(possibleWitness, int(remainder), p)

    if possibleWitness == 1 or possibleWitness == p - 1:
        return False

    for _ in range(exponent):
        possibleWitness = pow(possibleWitness, 2, p)

        if possibleWitness == p - 1:
            return False
        
        return True

def probablyPrime(p, accuracy=100):
    if p == 2 or p == 3: return True
    if p < 2: return False

    exponent, remainder = decompose(p - 1)

    for _ in range(accuracy):
        possibleWitness = random.randint(2, p - 2)
        if isWitness(possibleWitness, p, exponent, remainder):
            return False
    return True
