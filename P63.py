# -*- coding: utf-8 -*-


def find_powerful_count(k):
    '''
    对于一个幂次k
    找到n^k长度与k相同的所有n
    输出n的数目
    '''
    n = 1
    count = 0
    while True:
        length = len(str(n**k))
        if length < k:
            n += 1
        elif length == k:
            count += 1
            n += 1
        else:
            break
    return count

if __name__=='__main__':
    count = 0
    for i in range(1,50):
        num = find_powerful_count(i)
        if num > 0:
            count += num
        else:
            break
    print(count)
