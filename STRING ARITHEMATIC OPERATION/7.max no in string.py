def maxNoinString(s):
    l=[]
    res=''

    for x in s:
        if x.isdigit():
            res=res+x
        elif x.isalpha():
            if len(res)>0:
                l.append(int(res))
                res=''
    if len(res)>0:
        l.append(int(res))

    return max(l)
s='100klh564abc365bg'
print(maxNoinString(s))

s='abchsd0365sdhs'
print(maxNoinString(s))
