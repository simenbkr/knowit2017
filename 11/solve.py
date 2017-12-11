def isPal(x):
    return str(x)[::-1] == str(x)

def isPrime(x):
    for m in range(2, int(x**0.5)+1):
        if not x%m:
            return False
    return True

def isMIRP(x):
    if isPal(x): return False
    if isPrime(x) and isPrime(int(str(x)[::-1])):
        return True
    return False
s = 0
for i in xrange(13,1000,2):
    if isMIRP(i): s+= 1
print s
