def isPalindrome(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def makepalindrome(s):
    count=0
    while(isPalindrome(s)==False):
        count+=1
        s=s[:len(s)-1]

    print(count)



S = "LOL"
makepalindrome(S)

s='JAVA'
makepalindrome(s)