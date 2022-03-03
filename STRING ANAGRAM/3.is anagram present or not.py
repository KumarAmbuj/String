def findallpermute(arr,low,r,l):
    if low==r:
        l.append(''.join(arr))
    else:
        for i in range(low,r+1):
            arr[low],arr[i]=arr[i],arr[low]
            findallpermute(arr,low+1,r,l)
            arr[low],arr[i]=arr[i],arr[low]

def stringcontainsAnagram(s,patt):

    arr=list(patt)
    l=[]

    findallpermute(arr,0,len(arr)-1,l)

    hash=set(l)

    found=[]

    for x in hash:
        found.append(s.find(x))

    for x in found:
        if x!=-1:
            print('found at',x)

txt = "BACDGABCDA"
pat = "ABCD"

stringcontainsAnagram(txt,pat)


txt =  "AAABABAA"
pat = "AABA"

stringcontainsAnagram(txt,pat)