def isDivisible(s):
    res1=0
    res2=0

    for i in range(len(s)):
        if i%2==0:
            res1=res1+int(s[i])

        else:
            res2=res2+int(s[i])

    if (res1-res2)%11==0:
        return True
    else:
        return False

s='76945'
print(isDivisible(s))

s='1234567589333892'
print(isDivisible(s))

s='363588395960667043875487'
print(isDivisible(s))