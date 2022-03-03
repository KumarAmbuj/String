def findmaxconsecutive(s):
    ans=''
    m=-9
    prev=s[0]
    for i in range(1,len(s)):
        a=s[i]
        if a not in prev:
            if len(prev)>m:
                m=len(prev)
                ans=prev[0]
            prev=a
        elif a in prev:
            prev=prev+a

    if len(prev)>m:
        ans=prev[0]
    print(ans)


s='geeekk'
findmaxconsecutive(s)

s='aaaabbcbbb'
findmaxconsecutive(s)
