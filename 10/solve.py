"""
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]
[1,0,0,0,0,0,0,0,1,0,0,0,0
"""

a = [1 for i in range(1, 1501)]
last = True
while sum(a) > 1:
    for i in xrange(len(a)):
        if a[i] == 0: continue
        if not last and a[i] == 1:
            a[i] = 0
            last = True
        else:
            last = False
assert (a.index(1) + 1) == 953
print (a.index(1) + 1)
