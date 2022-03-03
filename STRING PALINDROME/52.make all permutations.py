def makepermutations(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    odd=0
    l=[]
    for x in hash:
        if hash[x]%2==1:
            odd+=1
        else:
            l.append(hash[x]//2)
    if odd>1:
        print('not possible')
        return


    n=sum(l)

    fact=[0 for i in range(n+1)]
    fact[0]=1

    for i in range(1,n+1):
        fact[i]=fact[i-1]*i

    div=1
    for i in range(len(l)):
        div=div*fact[l[i]]

    res=fact[n]//div
    print(res)
s = "gfgf"
makepermutations(s)

s = "aaaaaabbbb"
makepermutations(s)


