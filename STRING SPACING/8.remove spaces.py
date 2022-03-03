def shortform(s):
    res=''
    prev=''

    for x in s:
        if x!=' ':
            if len(prev)==0:
                prev=x
        elif x==' ':
            res=res+prev
            prev=''

    if len(prev)>0:
        res=res+prev
    print(res)

s="geeks for geeks"
shortform(s)

s='happy   coding'
shortform(s)