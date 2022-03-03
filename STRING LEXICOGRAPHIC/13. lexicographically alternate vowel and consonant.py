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


def makealternate(s):
    vowels='aeiou'

    vow=[]
    cons=[]
    for x in s:
        if x in vowels:
            vow.append(x)
        else:
            cons.append(x)
    if abs(len(vow)-len(cons))>1:
        print('not possible')
        return
    Quicksort(vow,0,len(vow)-1)
    Quicksort(cons,0,len(cons)-1)

    if len(vow)>len(cons):
        n1=len(vow)
        n2=len(cons)
        i=0
        j=0
        res=''
        while(j<n2):
            res=res+vow[i]
            res=res+cons[j]
            i+=1
            j+=1
        res=res+vow[i]
        print(res)

    elif len(vow)<len(cons):
        i=0
        n=len(vow)
        res=''
        while(i<n):
            res=res+cons[i]+vow[i]
            i+=1
        res=res+cons[i]
        print(res)
    elif len(vow)==len(cons):
        i=0
        n=len(vow)
        res=''
        if vow[0]<cons[0]:
            while(i<n):
                res=res+vow[i]+cons[i]
                i+=1
        elif cons[0]<vow[0]:
            while(i<n):
                res=res+cons[i]+vow[i]
        print(res)

makealternate('mango')
makealternate('aeroplane')
makealternate('abb')
makealternate('bbba')

