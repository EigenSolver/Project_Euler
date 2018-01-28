def count_rec(a, b):
    count = 0
    for m in range(1, a + 1):
        for n in range(1, b + 1):
            count += (a - m + 1) * (b - n + 1)
    return count

limit = 2000000

best = None
flag = 1000000
area = None
for i in range(1, 100):
    for j in range(1, 100):
        rec_num = count_rec(i, j)
        diff = abs(rec_num - limit)
        if diff < flag:
            flag = diff
            shape = (i, j)
            area = i * j
print('difference:{0}\nshape:{1}\nrec_num:{2}\narea:{3}'.format(
    flag, shape, count_rec(*shape), area))
