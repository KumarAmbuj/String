def isBothHalvesSame(s):

    n=len(s)
    s1=''
    s2=''
    if n%2==0:
        s1=s[:(n//2)]
        s2=s[n//2:]
    else:
        s1=s[:n//2]
        s2=s[(n//2)+1:]


    dic={}

    for x in s1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in s2:
        if x in dic:
            dic[x]-=1

    for x in dic:
        if dic[x]!=0:
            print('No')
            return
    print('Yes')

s='abbaab'
isBothHalvesSame(s)

s='abccba'
isBothHalvesSame(s)

s='abcba'
isBothHalvesSame(s)
