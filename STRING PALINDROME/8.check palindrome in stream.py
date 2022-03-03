def ispalindrome(s):
    i=0
    j=len(s)-1
    while(i<=j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def checkpalindromestream(s):
    res=''
    for x in s:
        res=res+x
        print('reading',x,end=' ')
        if ispalindrome(res):
            print('Yes')

        else:
            print('No')
    print('-----')
s="abcba"
checkpalindromestream(s)

s="aabaacaabaa"
checkpalindromestream(s)