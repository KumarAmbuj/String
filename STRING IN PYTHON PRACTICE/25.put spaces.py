def putspaces(s):
    i=1
    j=0
    l=[]

    while(i<len(s)):
        if s[i]==s[i].upper():
            l.append(s[j:i])
            j=i
        i+=1
    l.append(s[j:])
    ans=[]
    for x in l:
        ans.append(x[0].lower()+x[1:])

    print(' '.join(ans))

s='BruceWayneIsBatman'
putspaces(s)

s='GeeksForGeeks'
putspaces(s)
