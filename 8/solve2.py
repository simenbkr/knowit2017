dic = {1: True, 10: True, 9: False, 8: False, 7: True, 6: False, 5: False, 4: False, 3:False,2:False}
maks = 10**7
def juletall2(x):
    if x > maks:
        for n in curr_seq:
            dic[n] = False
        return False
    if x in dic:
        return dic[x]
    if x == 1:
        for n in curr_seq:
            dic[n] = True
        return True
    x2 = 0
    for i in str(x):
        x2 += int(i) ** 2
    curr_seq.append(x2)
    return juletall2(x2)

s = 0
for i in xrange(maks,0,-1):
    global curr_seq
    curr_seq = [i]
    if i in dic and dic[i]:
        s += i
        continue
    if juletall2(i):
        s+=i

print s





