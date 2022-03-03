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

def alternate(s):
    upp=[]
    low=[]
    for x in s:
        if x.islower():
            low.append(x)
        elif x.isupper():
            upp.append(x)

    Quicksort(upp,0,len(upp)-1)
    Quicksort(low,0,len(low)-1)

    i=0
    j=0
    res=''
    while(i<len(upp) and j<len(low)):
        res=res+upp[i]+low[j]
        i+=1
        j+=1
    if i<len(low):
        res=res+''.join(upp[i:])
    if j<len(low):
        res=res+''.join(low[j:])
    print(res)
s='bAwutndekWEdkd'
alternate(s)