def gcd(a, b):
    if b == 0:
        return a
        
    if a==1 or b == 1:
        return 1
    
    r = a % b
    return gcd(b, r)
    

def gcd2(a, b):
    if a < b:
        a, b = b, a
        
    if b == 0:
        return a
    return gcd2(a-b, b)



def gcd3(a, b):    
    if a == b:
        return a
    
    if a < b:
        a, b = b, a
    
    if a & 1 == 0 and b & 1 == 0: # 偶数
        return gcd(a>>1, b>>1)
    elif a & 1 == 0:
        return gcd(a>>1, b)
    elif b & 1 == 0:
        return gcd(a, b>>1)
    else:        
        return gcd(a-b, b)



import sys
sys.setrecursionlimit(100000)


import timeit

print(timeit.timeit("gcd(10000,1)", "from __main__ import gcd",  number=10000))
print(timeit.timeit("gcd3(10000,1)", "from __main__ import gcd3",  number=10000))
print(timeit.timeit("gcd2(10000,1)", "from __main__ import gcd2",  number=1))


