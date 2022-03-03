def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if ord(arr[j])<ord(x):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)


def Rearrange(s):
    l=[]
    res=0
    for x in s:
        if x.isdigit():
            res=res+int(x)

        else:
            l.append(x)

    Quicksort(l,0,len(l)-1)

    result=''.join(l)+str(res)
    print(result)

s = "ACCBA10D2EW30"
Rearrange(s)
