def find(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in hash:
        a=x+str(hash[x])
        print(a,end=' ')

s='geeksforgeeks'
find(s)
