def find2ndmostfrequent(arr):
    hash={}
    for x in arr:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    first=-9
    second=-9
    ans=''

    for x in hash:
        if hash[x]>first:
            second=first
            first=hash[x]
        elif hash[x]>second:
            second=hash[x]
            ans=x
    print(ans)
arr=["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
find2ndmostfrequent(arr)

arr=["geeks", "for", "geeks", "for", "geeks", "aaa"]
find2ndmostfrequent(arr)