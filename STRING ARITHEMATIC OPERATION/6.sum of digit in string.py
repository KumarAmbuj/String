def findSum(s):
    res=''
    l=[]

    for x in s:
        if x.isdigit():
            res=res+x
        elif x.isalpha():
            if len(res)>0:
                l.append(int(res))
                res=''

    if len(res)>0:
        l.append(int(res))

    return sum(l)
s='1abc23'
print(findSum(s))

s='1abc2x30yz67'
print(findSum(s))

