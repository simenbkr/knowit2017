for i in xrange(6,1000000,10):
    a = int(str(i)[-1] + str(i)[:-1])
    if a == 4*i:
        print i
        break
