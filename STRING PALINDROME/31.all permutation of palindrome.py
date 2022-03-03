def isPalindrome(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def permute(arr,s,path,l):
    if len(arr)==len(s):
        if isPalindrome(s):
            l.add(s)
        return
    if len(s)>len(arr):
        return

    for i in range(len(arr)):
        if i not in path:
            res=s+arr[i]
            path.append(i)
            permute(arr,res,path,l)
            path.pop()

def findallpermute(arr):
    res=''
    path=[]
    l=set()
    permute(arr,res,path,l)
    count=0
    for x in l:
        count+=1
        print(x,end=' ')
        if count==3:
            print()
            count=0
    print()


s= "aabcb"
findallpermute(s)

s="aabbcadad"
findallpermute(s)