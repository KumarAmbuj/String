def find(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    ans=0
    for x in hash:
        ans+=hash[x]*hash[x]
    print(ans)

find('geeksforgeeks')