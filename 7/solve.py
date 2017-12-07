alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
crypt = "OTUJNMQTYOQOVVNEOXQVAOXJEYA"
def enc(stri):
    ret = ''
    for i in range(len(stri)):
        ret += alf[(ord(stri[i]) + 2*alf.index(stri[i]) + 1) % len(alf)]
    return ret

print enc(enc(crypt))
assert enc("JULEMANN") == "PWVAYOBB"
