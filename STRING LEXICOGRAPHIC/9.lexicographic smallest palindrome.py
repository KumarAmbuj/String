def ispalindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:

            return False
        i+=1
        j-=1
    return True

def possible(arr,s,i,n):
    if i==n:

        if ispalindrome(s):
            print(s)
            return True
        return False
    if i>n:
        return False

    if( ord(arr[i])>=ord('a') and ord(arr[i])<=ord('z')):
        res=s+arr[i]
        return possible(arr,res,i+1,n)

    else:
        for k in range(26):
            res=s+chr(ord('a')+k)
            if possible(arr,res,i+1,n):
                return True
    return False

def findlexicosmallestPalindrome(arr):
    res=''
    i=0
    n=len(arr)
    if possible(arr,res,i,n)==False:
        print('not possible')

s="bc*b"
findlexicosmallestPalindrome(s)

s="bc*a*cb"
findlexicosmallestPalindrome(s)

s = "bac*cb"
findlexicosmallestPalindrome(s)


s = "ba*cc*b"
findlexicosmallestPalindrome(s)

