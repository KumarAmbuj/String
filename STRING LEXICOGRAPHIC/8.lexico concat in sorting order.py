def findpermute(arr,i,s,l,n):

    if len(s)>0:
        l.append(s)

    for k in range(i,n):
        res=s+arr[k]
        findpermute(arr,k+1,res,l,n)
def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)


def lexicosmallest(arr):
    l=[]
    res=''
    n=len(arr)
    findpermute(arr,0,res,l,n)

    Quicksort(l,0,len(l)-1)

    res=''
    for i in range(len(l)):
        res=res+l[i]
    print(res)
lexicosmallest('abc')
lexicosmallest('cba')