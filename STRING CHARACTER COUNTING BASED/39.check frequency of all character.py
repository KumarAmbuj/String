def allSame(hash,s):
    same=0
    for x in hash:
        if hash[x]>0:
            same=hash[x]
            break

    for x in hash:
        if x!=s and hash[x]!=same:
            return False
    return True

def makeallsame(s):
    hash={}

    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in hash:

        hash[x]-=1

        if allSame(hash,x):
            return True
        hash[x]+=1
    return False
s = "xyyzz"
print(makeallsame(s))

s='xxxxyyzz'
print(makeallsame(s))

s='xyyzz'
print(makeallsame(s))