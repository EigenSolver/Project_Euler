from Euler_Lib import gcd


def phi_n(n):
    total = 1
    for i in range(2, n):
        if gcd(n, i) == 1:
            total += 1
    return n / total

num = 0
flag = 0
for i in range(2, 1000001):
    ratio = phi_n(i)
    if ratio > flag:
        flag = ratio
        num = i

print('ratio:{0}\nnumber:{1}'.format(flag, num))
