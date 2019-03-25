from fractions import Fraction

low_bound=0.425
up_bound=0.43
max_range=1000000

candidate=[]

print('searching candidates...')
print('progress: ')
for i in range(2,max_range+1):
    for j in range(int(low_bound*i),int(up_bound*i)+1):
        if i%100000==0:
            print('#',end='')
        candidate.append(Fraction(j,i))

print('total size of array: {}'.format(len(candidate)))
command=input('sort the arry[y/n]?')
if command=='y':
    print('start sorting...')
    candidate.sort()
    loc=candidate.index(Fraction(3,7))
    print("the location of 3/7 is {}".format(loc))
    print("the latest neighbor is {}".format(candidate[loc-1]))
elif command=='n':
    print('end')
else:
    exit()


