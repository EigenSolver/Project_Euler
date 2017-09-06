string=''

n=1
while len(string)<1000000:
    string+=str(n)
    n+=1
    

result=1
for i in range(7):
    result*=int(string[10**i-1])

print(result)