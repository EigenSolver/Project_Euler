from Euler_Lib import combinationN
from decimal import Decimal,getcontext

getcontext().prec=10

cacheF=[1]
for n in range(3,8):
    cacheF.append(combinationN(10*n,20)-sum([combinationN(n,i)*cacheF[i-2] for i in range(2,n)]))


def F(n):
    return cacheF[n-2]


A=sum([n*combinationN(7,n)*F(n) for n in range(2,8)])
B=combinationN(70,20)

P=Decimal(str(A))/Decimal(str(B))
print(P)
