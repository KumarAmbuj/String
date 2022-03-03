def findmaxsum(s):
    res=0

    for x in s:
        if x=='0' or x=='1' or res<2:
            res=res+int(x)
        else:
            res=res*(int(x))
    return res

s='01231'
print(findmaxsum(s))

s="01891"
print(findmaxsum(s))