l = [1,2,2]
def gullrekka():
    for n in range(3,1000000):
        ll = [n]*(l[n-1])
        l.extend(ll)
        if len(l) >= 1000000:
            return sum(l[:1000000])

print gullrekka()
