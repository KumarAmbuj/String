def notpalindrome(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!='.' and s[n-1-i]!='.' and s[i]!=s[n-1-i]:
            return False



def makePalindrome(s):

    if notpalindrome(s)==False:
        print('not possible')
        return


    l=list(s)
    n=len(s)

    for i in range(len(l)):

        if l[i]=='.':

            if l[n-1-i]!='.':
                l[i]=l[n-1-i]
            else:
                l[i]=l[n-1-i]='a'

    print(''.join(l))

s = "ab..e.c.a"
makePalindrome(s)

s='ab..e.c.b'
makePalindrome(s)