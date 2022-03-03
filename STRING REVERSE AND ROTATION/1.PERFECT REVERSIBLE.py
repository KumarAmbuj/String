#just check is palindrome or not
def isperfectReversible(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

str = "aba"
if (isperfectReversible(str)):
    print("YES")
else:
    print("NO")

def isReversible(s):
    for i in range(len(s)-1):
        res=s[i]
        for j in range(i+1,len(s)):
            res=res+s[j]
            rev=res[::-1]
            if rev not in s:
                return False
    return True


str = "aba"
if (isReversible(str)):
    print("YES")
else:
    print("NO")
