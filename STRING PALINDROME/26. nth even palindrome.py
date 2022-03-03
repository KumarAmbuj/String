def findpalindrome(s):
    res=s

    for i in range(len(s)-1,-1,-1):
        res=res+s[i]
    print(res)

findpalindrome('12')
