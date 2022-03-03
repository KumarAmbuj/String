def isPalindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def countpalindrome(s):
    count=0

    for i in range(len(s)-1):
        res=s[i]
        count+=1
        for j in range(i+1,len(s)):
            res=res+s[j]
            if isPalindrome(res):
                count+=1
    count+=1
    print(count)


def findcount(s,arr):
    for i in range(len(arr)):
        countpalindrome(s[arr[i][0]:arr[i][1]+1])


s = "xyaabax"

arr=[(3,5),(2,3)]

findcount(s,arr)