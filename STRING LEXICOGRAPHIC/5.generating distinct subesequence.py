def permute(arr,s,i,n):

    if len(s)>0:
        print(s)

    for k in range(i,n):
        res=s+arr[k]
        permute(arr,res,k+1,n)

def lexicographicorder(s):
    arr=''.join(sorted(s))
    res=''
    n=len(arr)
    permute(arr,res,0,n)

lexicographicorder('xyzx')