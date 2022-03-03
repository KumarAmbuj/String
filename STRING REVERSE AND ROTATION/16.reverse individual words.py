def findreverse(s):
    res=''
    prev=''
    for i in range(len(s)):
        if s[i]==' ':
            res=res+prev[::-1]+' '
            prev=''
        else:
            prev=prev+s[i]
    if len(prev)>0:
        res=res+prev[::-1]
    print(res)

s='Geeks for Geeks'
findreverse(s)