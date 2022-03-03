def putspaces(s):
    res=''
    prev=''

    for x in s:
        if x.isupper():
            res=res+' '+prev
            prev=x.lower()
        else:
            prev=prev+x
    if len(prev)>0:
        res=res+' '+prev

    print(res)

s='BruceWayneIsBatman'
putspaces(s)
