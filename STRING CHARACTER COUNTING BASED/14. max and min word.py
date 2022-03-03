def findMaxMinWords(s):
    l=s.split()
    mn=99
    mns=''

    mx=-9
    mxs=''

    for x in l:
        if len(x)<mn:
            mn=len(x)
            mns=x
        if len(x)>mx:
            mx=len(x)
            mxs=x
    print('max len is ',mxs)
    print('min len is ',mns)

s='GeeksforGeeks A computer Science portal for Geeks'
findMaxMinWords(s)


def findMinMaxWords(s):
    mn=99
    mns=''
    mx=0
    mxs=''
    i=0
    prev=''
    while(i<len(s)):

        if s[i]==' ':

            if len(prev)<mn:
                mn=len(prev)
                mns=prev
            if len(prev)>mx:
                mx=len(prev)
                mxs=prev
            prev=''

        else:
            prev=prev+s[i]
        i+=1

    if prev!='':
        if len(prev) < mn:
            mn = len(prev)
            mns = prev
        if len(prev) > mx:
            mx = len(prev)
            mxs = prev

    print('max len is',mxs)
    print(' min len is',mns)

s='GeeksforGeeks A computer Science portal for Geeks'
findMinMaxWords(s)

