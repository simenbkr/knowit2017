for i in xrange(6,1000000,10):
    if int(str(i)[-1] + str(i)[:-1]) == 4*i:
        print i
        break
