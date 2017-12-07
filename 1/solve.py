#!/usr/bin/python

letters = 'aeteesasrsssstaesersrrsse'
sort_ = ''.join(sorted(letters))
print sort_


def ngram(word,n):
    return ''.join(map(''.join,zip(*[word[i:] for i in range(n)])))

def validcand(word):
    for letter in word:
        if letter not in letters:
            return False
    return True

def filter():
    kands = []
    with open('wordlist.txt','r') as f:
        for line in f.readlines():
            if validcand(line.strip()):
                kands.append(line.strip())
        f.close()

    with open('new.txt','w') as f:
        f.write('\n'.join(kands))
        f.close()

def getKands():

    with open('new.txt','r') as f:
        cands = [x.strip().strip('\n') for x in f.readlines()]
        f.close()
    return cands


def main():

    #filter()

    cands = getKands()
    assert ngram('snowflake',2) == 'snnoowwffllaakke'
    assert ngram('mistletoe',3) == 'misiststltleletetotoe'
    assert ''.join(sorted('fnaewkfonklsawlo')) == ''.join(sorted(ngram('snowflake',2)))

    for word in cands:
        for i in range(2,10):
            if ''.join(sorted(ngram(word,i))) == sort_:
                print i,word


if __name__ == '__main__':
    main()

