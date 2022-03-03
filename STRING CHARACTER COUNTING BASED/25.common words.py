def findcommonwords(arr):
    hash={}

    for x in arr:
        s=set(x)

        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
    prev=''
    for x in hash:
        if hash[x]==len(arr):
            prev=prev+x
    prev=sorted(prev)
    for x in prev:
        print(x,end=' ')

strings = [ "geeksforgeeks", "gemkstones",
            "acknowledges", "aguelikes" ]
findcommonwords(strings)

print()
arr=['apple',
         'orange']
findcommonwords(arr)