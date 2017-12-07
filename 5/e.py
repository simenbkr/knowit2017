l = [1,2]
def gullrekka():
    for n in range(1,1000000):
        ll = [n]*(l[n-1] - l.count(n))
        l.extend(ll)
        if len(l) >= 1000000:
            return sum(l[:1000000])

print gullrekka()
