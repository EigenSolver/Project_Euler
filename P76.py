def countSummation(n,m=None):
    if not m:
        m=n-1
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        if m==1:
            return 1
        else:
            return countSummation(n-m,m)+countSummation(n,m-1)
    
print(countSummation(100))
