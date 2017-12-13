def thue_morse_digits(digits):
    return  [bin(n).count('1') % 2 for n in range(digits)]

with open('loot.txt','r') as f:
    lines = [int(x.strip().strip('\n').split(',')[1].strip()) for x in f.readlines()]
    f.close()

s = sorted(lines)[::-1]
thue_seq = thue_morse_digits(len(s))
su = 0
for i in xrange(len(s)):
    if thue_seq[i] == 1:
        su += s[i]

print su
