def isDivisible(s):
    if len(s)==1:
        if int(s)%4==0:
            return True
        else:
            return False

    a=int(s[-2])*10 + int(s[-1])
    if a%4==0:
        return True
    else:
        return False

s='1124'
print(isDivisible(s))

s='363588395960667043875487'
print(isDivisible(s))