def makestring(n,k):
    res=''
    for i in range(k):
        res=res+chr(ord('a')+i)

    count=0
    for i in range(n-k):
        res=res+chr(ord('a')+count)
        count+=1
        if count==k:
            count=0
    return res

n = 5
k = 2
print(makestring(n, k))




