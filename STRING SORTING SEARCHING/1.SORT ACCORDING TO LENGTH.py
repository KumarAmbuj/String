def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if len(arr[j])<len(x):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def sortstring(s):
    l=s.split()

    Quicksort(l,0,len(l)-1)
    print(' '.join(l))

s="GeeksforGeeeks I from am"
sortstring(s)