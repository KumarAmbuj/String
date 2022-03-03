def findpermute(arr,s,n,count,k,path):
    if count[0]>=k:
        return
    if len(s)>=n:
        count[0]+=1

        if count[0]==k:
            print(s)
        return

    for i in range(len(arr)):
        if i not in path:
            res=s+arr[i]
            path.append(i)
            findpermute(arr,res,n,count,k,path)
            path.pop()


def findnthstring(arr,k):

    arr=''.join(sorted(arr))
    res=''
    path=[]
    count=[0]
    n=len(arr)
    findpermute(arr,res,n,count,k,path)

findnthstring('abc',3)
findnthstring('aba',2)
