def findKthNonrepeating(s,k):
    hash={}
    count=0
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1
    ans='-1'
    for x in hash:
        if hash[x]==1:
            count+=1

        if count==k:
            print(x)
            break
    else:
        print('not found')
s='geeksforgeeks'
k=3
findKthNonrepeating(s,k)

s='geeksforgeeks'
k=2
findKthNonrepeating(s,k)

s='geeksforgeeks'
k=4
findKthNonrepeating(s,k)