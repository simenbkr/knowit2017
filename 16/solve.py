with open('prisoners.txt','r') as f:
    rekke = [int(x.strip().strip('\n')) for x in f.readlines()]
light = False
flicks = [0] * 100
m = 0
for i in xrange(len(rekke)):
    indeks = rekke[i] -1
    if indeks == 0 and light:
        light = False
        flicks[indeks] += 1
    if flicks[indeks] == 0 and not light:
        light = True
        flicks[indeks] +=1
    m+=1
    if flicks[0] >= 99:
        break

assert m == 10553
print m
