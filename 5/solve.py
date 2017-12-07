dic = {}
def main():
    s = 1
    a = [1]
    dic[1] = 1
    for i in xrange(1000000 - 1):
        n = a[i]
        count = a[n-1]
        if dic[n] < count:
            dic[n] += 1
            a.append(n)
            s += n
            continue
        n += 1
        dic[n] = 1
        s += n
        a.append(n)
    print s

if __name__ == '__main__':
    main()
