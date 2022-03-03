def findalloccurrence(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    res=''
    for x in hash:
        res=res+x*hash[x]
    print(res)

s='geeksforgeeks'
findalloccurrence(s)