# -*- coding: utf-8 -*-
import numpy as np
import time

#set_89=set([89])
#set_1=set([1])
#

def digs_square(n):
    count=0
    while n!=0:
        count+=(n%10)**2
        n=n//10
#    for i in str(n):
#        count+=int(i)**2
    return count

begin_time=time.time()
chain=set()
end=10**7
step=end//50
domain=np.zeros(end)
domain[0]=1
domain[88]=89

for i in range(end):
    if i%step==0:
        print("{0}/{1} has finished!".format(i+step,end))
    if domain[i]!=0:
        continue
    else:
        nex=i+1
        chain.add(nex)
        while True:
            nex=digs_square(nex)
            if domain[nex-1]==1:
                for j in chain:
                    domain[j-1]=1
                chain=set()
                break
            if domain[nex-1]==89:
                for j in chain:
                    domain[j-1]=89
                chain=set()
                break
            chain.add(nex)

end_time=time.time()

print("\nresult: {}\n".format(np.sum(domain==89)))

print("time spend: {}".format(end_time-begin_time))
            