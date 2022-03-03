def findCombinations(color,s,l,left):
    if len(s)==left:
        l.append(s)
        return
    if len(s)>left:
        return

    for i in range(len(color)):
        res=s+color[i]
        findCombinations(color,res,l,left)


def findfactorial(s,n,fact):

    dic={}
    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    res=1

    for x in dic:
        if dic[x]>1:
            res=res*fact[dic[x]]

    return fact[n]//(res)







def findnoofString(n,r,b,g):
    res='r'*r+'b'*b+'g'*g
    color=['r','g','b']

    left=n-(r+g+b)

    l=[]
    s=''

    findCombinations(color,s,l,left)



    fact=[0]*(n+1)
    fact[0]=1

    for i in range(1,n+1):
        fact[i]=fact[i-1]*i

    sum = 0

    for x in l:
        sum=sum+findfactorial(res+x,n,fact)

    print(sum)

n = 4
r = 2
b = 0
g = 1
findnoofString(n, r, b, g)

n = 4
r = 1
b = 1
g = 1
findnoofString(n, r, b, g)


