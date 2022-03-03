def findallpermute(word,i,n):
    if i==n:
        print(word)
        return

    s=word[0:i]+' '+word[i:]
    findallpermute(s,i+2,len(s))

    s=word[0:i]+word[i:]
    findallpermute(s,i+1,len(s))






def applyspaces(arr):
    l=[]
    res=' '
    findallpermute(arr,1,len(arr))


applyspaces('ABC')