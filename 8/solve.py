
def getSeq(x):
    n = [x]
    tmp = x
    while tmp > 9:
        print tmp
        tmp2 = 0
        for i in str(tmp):
            tmp2 += int(i)**2
        tmp = tmp2
        n.append(tmp)

    return n

maks = 10 ** 7
dic = {}
def juletall(x):
    if x in dic:
        return dic[x] == 1
    tmp = x
    while tmp > 9:
        tmp2 = 0
        for i in str(tmp):
            tmp2 += int(i)**2
        if tmp2 in dic:
            return dic[tmp2] == 1
        tmp = tmp2

        if tmp > maks: return False
    dic[x] = tmp
    return tmp == 1

dic2 = {maks:False, 1:True, 13:True, 10:True}
def juletall2(x):
    if x > maks:
        for n in curr_seq:
            dic2[n] = False
        return False
    if x in dic2:
        return dic2[x]
    if x == 1:
        for n in curr_seq:
            dic2[n] = True
        return True
    if x < 10:
        for n in curr_seq:
            dic2[n] = False
        return False

    x2 = 0
    for i in str(x):
        x2 += int(i) ** 2
    curr_seq.append(x2)
    return juletall2(x2)



s = 0
for i in xrange(maks):
    global curr_seq
    curr_seq = [i]
    if i in dic2 and dic2[i]:
        s += i
        continue
    if juletall2(i):
        s+=i

print s
