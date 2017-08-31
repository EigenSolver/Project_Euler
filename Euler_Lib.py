# -*- coding: utf-8 -*-

from P3 import prime_factorization,gcd
from P4 import palindromeQ
from P5 import lcm
from P7 import eratosthenes
from P8 import product
from P12 import triangle_number,find_factors,num_of_factors
from P15 import factorial,step_factorial,combination
from P17 import gimmeThemWords
from P21 import sum_factors
from P23 import abundantQ
from P28 import sprial_number
from P37 import trunctableQ
from P38 import pandigitalQ

def permutations(string):
    if len(string)<2:
        return string

    result=[]
    for i in range(len(string)):
        remain=string[:i]+string[i+1:]
        letter=string[i]
        result+=list(map(lambda x: letter+x,permutations(remain)))
    return result


