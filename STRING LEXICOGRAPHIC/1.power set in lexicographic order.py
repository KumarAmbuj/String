def findpermute(arr,s,i,n):



    if len(s)>0:
        print(s)

    for k in range(i,n):
        res=s+arr[k]

        findpermute(arr,res,k+1,n)


def findpowerset(arr):
    arr=''.join(sorted(arr))
    res=''
    n=len(arr)
    findpermute(arr,res,0,n)

findpowerset('abc')