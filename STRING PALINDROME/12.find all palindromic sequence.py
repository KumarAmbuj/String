def isPalindrome(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def findPalindromicSequence(s,i,path,l,n):
    if i>=n:
        if len(path)>0:
            if isPalindrome(path):
                x=path.copy()
                l.append(x)
        return

    path.append(s[i])

    findPalindromicSequence(s,i+1,path,l,n)

    path.pop()

    findPalindromicSequence(s,i+1,path,l,n)




def findAllPalindromicSequence(s):
    l=[]
    path=[]
    n=len(s)

    findPalindromicSequence(s,0,path,l,n)

    print(len(l))

findAllPalindromicSequence('abcd')

findAllPalindromicSequence('aab')

findAllPalindromicSequence('aaaa')