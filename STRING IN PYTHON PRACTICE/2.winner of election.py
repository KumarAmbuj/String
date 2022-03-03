def findwinner(arr):
    dic={}

    for x in arr:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    m=0
    ans=''
    for x in dic:
        if dic[x]>m:
            m=dic[x]
            ans=x

    return ans





votes = ["john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"]

print(findwinner(votes))
