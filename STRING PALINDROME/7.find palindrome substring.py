def ispalindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def findallpalindrome(s):

    l=[]

    for i in range(len(s)-1):
        l.append(s[i])
        res=s[i]
        for j in range(i+1,len(s)):
            res=res+s[j]
            if ispalindrome(res):
                l.append(res)
    l.append(s[-1])
    print(','.join(l))

findallpalindrome('hellolle')

findallpalindrome('geeksforgeeks')