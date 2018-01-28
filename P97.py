

result=2**60
for i in range(7830457-60):
    result=int(str(2*result)[-10:])

print(int(str(28433*result+1)[-10:]))
