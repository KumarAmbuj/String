def findmaxxor(a):
    ans=-9999

    for i in range(len(a)):
        cur=0

        for j in range(i,len(a)):
            cur=cur^a[j]
            ans=max(ans,cur)

    return ans
arr = [8, 1, 2, 12]
print(findmaxxor(arr))
