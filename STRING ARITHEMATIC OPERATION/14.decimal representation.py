def isDivisible(s):
    s=s[::-1]

    res=0

    for i in range(len(s)):
        res=res+int(s[i])*(2**i)

    if res%5==0:
        return True
    else:
        return False

s='10000101001'
print(isDivisible(s))