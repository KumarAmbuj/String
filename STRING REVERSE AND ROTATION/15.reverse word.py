def reverseword(s):
    res=''
    prev=''
    for i in range(len(s)):
        if s[i]==' ':
            res=' '+prev+res
            prev=''
        else:
            prev=prev+s[i]
    if len(prev)>0:
        res=prev+res
    print(res)

s = "geeks quiz practice code"
reverseword(s)