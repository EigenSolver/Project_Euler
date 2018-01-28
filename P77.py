from Euler_Lib import eratosthenes


def primeSummation(n, lis=None):
    if not lis:
        lis = tuple(eratosthenes(n))
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if len(lis) == 1:
            if n % lis[0] == 0:
                return 1
            else:
                return 0
        else:
            return primeSummation(n - lis[-1], lis) + primeSummation(n, lis[:-1])


for i in range(7,100):
    if primeSummation(i)>5000:
        print(i)
        break
        
