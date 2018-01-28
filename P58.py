from Euler_Lib import probablyPrime
from math import sqrt
import datetime
#%%
def genFstDiagonal(n):
    temp = 1
    for i in range(n + 1):
        delta = 8 * i + 2
        step = 2 * (i + 1)
        temp += delta
        yield (temp + step * np.arange(4))

def isPrime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True
#%%
#
#start=datetime.datetime.now()
#is_prime = eratosthenes(200000000, 0, True)[1]
#end=datetime.datetime.now()
#print("time waste:",(end-start))

#%%

m = 3
square = genFstDiagonal(m)
count = 0

for n in range(m):
    for i in next(square):
        count += isPrime(int(i))
    al=(4 * n + 5)
    ratio = count / al
    print(count,al)
    if ratio < 0.1:
        print("ratio:{0}\nlayer:{1}".format(ratio, 2 * n + 3))
        break
