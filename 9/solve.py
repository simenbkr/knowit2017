def count(n):
    count = 0
    length = 1
    while( length * (length + 1) < 2 * n):
        a = (1.0 * n - (length * (length + 1) ) / 2) / (length + 1)
        if (a - int(a) == 0.0):
            count += 1
        length += 1
    return count

s = 0
for i in xrange(1,130001):
    s += count(i)

print s
