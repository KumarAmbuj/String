def permute(arr,s,i,l):
    if i==len(arr):
        l.append(s)
        return
    if i>len(arr):
        return

    res=s+arr[i].upper()
    permute(arr,res,i+1,l)

    res=s+arr[i].lower()
    permute(arr,res,i+1,l)

def findpermute(arr):

    l=[]
    s=''
    permute(arr,s,0,l)

    print(' '.join(l))

s="AB"
findpermute(s)

s="ABc"
findpermute(s)