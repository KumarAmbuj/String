def distribute(s,k):

    hash={}

    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

        if hash[x]>k:
            return False
    return True

s='aabb'
k=2
print(distribute(s,k))

s='aacaab'
k=3
print(distribute(s,k))
