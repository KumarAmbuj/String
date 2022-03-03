def permute(arr,l,r,s):
    if l==r:
        s.add(''.join(arr))
    else:
        for i in range(l,r+1):
            arr[l],arr[i]=arr[i],arr[l]
            permute(arr,l+1,r,s)
            arr[l],arr[i]=arr[i],arr[l]

def findpermutations(arr):
    arr=list(arr)
    s=set()

    permute(arr,0,len(arr)-1,s)

    for x in s:
        print(x)
s='ABA'
findpermutations(s)

