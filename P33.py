# -*- coding: utf-8 -*-

from P3 import gcd

fractions=[]

for i in range(10,100):
    for j in range(10,i):
        fractions.append((j,i))
        
print('fractions produced!')

def digit_cancel(fraction):
    up,down=tuple(map(str,fraction))
    for n in range(1,10):
        char=str(n)
        if (char in up) and (char in down):
            up=up.replace(char,'')
            down=down.replace(char,'')
    try:
        return (int(up),int(down))
    except:
        return 1

def simplify(fraction):
    up,down=fraction
    return up/down
#    g=gcd(up,down)
#    return (up//g,down//g)


result=[]
for f in fractions:
    cancel=digit_cancel(f)
    if gcd(f[0],f[1])==1:
        continue
    else:
        if cancel==f:
            continue
    try:
        if cancel[0]/cancel[1]==simplify(f):
            result.append(f)
    except:
        continue

print(result)

up=down=1
for i in result:
    up=up*i[0]
    down=down*i[1]
g=gcd(up,down)
print(up//g,down//g)
