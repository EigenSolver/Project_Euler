from functools import reduce

#最小共倍数算法

def lcm(a,b):
    assert (a,b)!=(0,0)
    temp = a 
    while temp%b !=0:
        temp+=a
    return temp

    
if __name__=='__main__':
    print(reduce(lcm,range(1,21)))
