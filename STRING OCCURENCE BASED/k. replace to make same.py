def makeallsame(s,k):
    if len(s)%k!=0:
        return False
    i=0
    l=[]
    prev=''

    for x in s:
        prev=prev+x
        i+=1

        if i==k:
            l.append(prev)
            prev=''
            i=0

    hash={}
    for x in l:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    if len(hash)>2:
        return False

    for x in hash:
        if hash[x]==1:
            return True
    return False

s = "bdac"
k = 2
print(makeallsame(s,k))

s = "abcbedabcabc"
k = 3
print(makeallsame(s,k))

s = "bcacc"
k = 3
print(makeallsame(s,k))

s = "bcacbcac"
k = 2
print(makeallsame(s,k))

s = "bcdbcdabcedcbcd"
k = 3
print(makeallsame(s,k))


