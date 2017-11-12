# -*- coding: utf-8 -*-

import fractions

def expansion(n):
    if n==1:
        return fractions.Fraction(1,2)
    else:
        return fractions.Fraction(1,2+expansion(n-1))
    
expansions=list(range(1001))
expansions[0]=fractions.Fraction(1,2)

for n in range(1,1001):
    expansions[n]=fractions.Fraction(1,2+expansions[n-1])


count=0
for f in expansions:
    f+=1
    if len(str(f.numerator))>len(str(f.denominator)):
        count+=1
