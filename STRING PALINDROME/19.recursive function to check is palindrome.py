def ispalindrome(s,i,j):
    if i==j:
        return True
    if i>j:
        return True

    if s[i]==s[j]:
        if ispalindrome(s,i+1,j-1):
            return True
    else:
        return False



def checkpalindrome(s):
    if ispalindrome(s,0,len(s)-1):
        print('Yes')
    else:
        print('No')

s='malayxalam'
checkpalindrome(s)
