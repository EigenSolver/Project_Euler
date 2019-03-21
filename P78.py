def p(n, k):
    '''
    n: number of total coins
    k: max component

    the problem is try to find all the possible combination of numbers that added up equals n, 
    partitions of a number 'n' equals p(n,n),
    n can be made up with components from {1,2,3...n}, for example n=5=4+1 or 3+2
    p(n,k) can be divided into two parts, p(n-k,k) and p(n,k-1), which can be solved using recursion once we know p(n,1)=1

    '''
    if k == 1 or n==0:
        return 1
    elif k < 1:
        return 0
    elif k > n:
        return p(n,n)
    else:
        return p(n-k,k)+p(n,k-1)

# def partitions(n):
#     return p(n, n)
    
#print(list(map(partitions, range(1, 8))))

'''search of 1m'''

def report(n, temp):
    print("current n: {0}, partitions: {1}".format(n, temp))


'''after cheating with Wikipedia '''

def pentagonal(i):
    return (3 * i ** 2 - i) //2

partitions = [0,1]
n = 2
target=1000000
while True:
    total=0
    i = 1
    while pentagonal(i)<n:
        total += (-1)**(i - 1) * partitions[n - pentagonal(i)]
        i += 1
    i = 1
    while pentagonal(-i)<n:
        total += (-1)**(-i - 1) * partitions[n - pentagonal(-i)]
        i += 1

    partitions.append(total % target)
    if partitions[n] == 0:
        print(n-1)
        break
    n += 1
    