def isPalindrome(s):

    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def isRotationPalindrome(s):

    res=''

    for x in s:
        if x.isalnum():
            res=res+x

    if isPalindrome(res):
        return 1

    for i in range(1,len(res)):

        s=res[i:]+res[:i]

        if isPalindrome(s):
            return 1
    return 0

s = "aaaad"
print(isRotationPalindrome(s))

s = "abcd"
print(isRotationPalindrome(s))




