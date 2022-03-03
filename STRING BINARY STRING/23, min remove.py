def minremove(s):
    prev=s[0]

    res=0

    for i  in range(1,len(s)):
        if s[i] not in prev:

            if len(prev)>1:
                res=res+len(prev)-1
            prev=s[i]
        elif s[i] in prev:
            prev=prev+s[i]
    if len(prev)>1:
        res=res+len(prev)-1
    print(res)
minremove('000111')
s = "01010101"
minremove(s)
minremove('1111')