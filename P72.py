from Euler_Lib import eratosthenes,gcd,prime_factorization
from datetime import datetime

limit=9
count=0
view=True
visual=[]

start=datetime.now()

print("Generating primes....")
primes=set(eratosthenes(limit))
print("Done")

for d in range(2,limit+1):
#    if d%(limit//10)==0:
#        print("{}0%".format(d//(limit//10)))
    if d in primes:
        count+=d-1
        if view:
            visual.extend(["{0}/{1}".format(n,d) for n in range(1,d)])
    else:
        factors=prime_factorization(d,primes)
        for n in range(1,d):
            if n==1:
                count+=1
                visual.append("{0}/{1}".format(n,d))
            elif n in primes:
                if d%n!=0:
                    count+=1
                    visual.append("{0}/{1}".format(n,d))
            else:
                if all([n%(f[0]) for f in factors]):
                    count+=1
                    visual.append("{0}/{1}".format(n,d))
#            elif gcd(n,d)==1:
#                count+=1
#                if view:
#                    visual.append("{0}/{1}".format(n,d))
#            else:
#                continue
end=datetime.now()

print(count)
print("Time consuming: {}".format(end-start))
if view:
    print(visual)
                
        
    
    
    