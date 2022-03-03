def permute(arr,s,l,n):
    if len(s)==n:
        l.append(s)
        return
    if len(s)>n:
        return

    for i in range(len(arr)):
        res=s+arr[i]
        permute(arr,res,l,n)

def findpermute(arr):
    l=[]
    res=''

    permute(arr,res,l,len(arr))

    for x in l:
        print(x,end=' ')
    print()

s='AB'
findpermute(s)

s="ABC"
findpermute(s)
