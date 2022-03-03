def isdivisible(s):
    n=len(s)
    if n%3!=0:
        k = 3 - n % 3
        s = '0' * k + s
    n=len(s)
    res=0
    i=0
    j=3

    while(i<n):
        res=res+int(s[i:i+3])
        i+=3
    if res%999==0:
        return True
    else:
        return False

s='235764'
print(isdivisible(s))


s='1998'
print(isdivisible(s))

s='23576'
print(isdivisible(s))

s='1244633121'
print(isdivisible(s))



