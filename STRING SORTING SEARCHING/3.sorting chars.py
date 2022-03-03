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
def sortingchar(s):
    l=list(s)

    Quicksort(l,0,len(l)-1)

    print(''.join(l))

s='bbccdefbbaa'
sortingchar(s)
s='geeksforgeeks'
sortingchar(s)



def method2(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1
    l=[]
    for x in hash:
        l.append(x)
    Quicksort(l,0,len(l)-1)

    res=''
    for x in l:
        res=res+x*hash[x]
    print(res)

s='bbccdefbbaa'
method2(s)
s='geeksforgeeks'
method2(s)