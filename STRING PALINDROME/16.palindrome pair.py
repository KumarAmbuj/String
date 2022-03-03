def isPalindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def findpairutil(arr,s,path):
    if len(path)==2:
        if isPalindrome(s):
            return True
        return False
    if len(path)>2:
        return False

    for i in range(len(arr)):
        if i not in path:
            res=s+arr[i]
            path.append(i)
            if findpairutil(arr,res,path):
                return True
            path.pop()
    return False

def findpair(arr):
    res=''
    path=[]
    if findpairutil(arr,res,path):
        print('Yes')
        return
    print('No')


arr = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
findpair(arr)


arr = ["abc", "xyxcba", "geekst", "or",
                                      "keeg", "bc"]
findpair(arr)