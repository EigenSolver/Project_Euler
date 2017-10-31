import numpy as np

def permuteQ(str1,str2):
    if all([i in str2 for i in str1]):
        return True
    else:
        return False

def gen_domain(init,length):
    domain=np.zeros(0)
    for i in range(init,length+1):
        start=10**(i-1)
        limit=10**i
        domain=np.hstack([domain,np.arange(start,limit//6+1)])
    return domain.astype(int)

domain=gen_domain(4,7)
for i in domain:
    if all([permuteQ(str(i),str(n*i)) for n in (2,3,4,5,6)]):
        print(i)
        break