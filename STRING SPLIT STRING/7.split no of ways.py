def findnoofways(s):
    char=[0]*26

    for x in s:
        char[ord(x)-ord('a')]+=1

    ans=1

    for i in range(26):
        if char[i]!=0:
            ans=ans*char[i]

    print(ans)
s = "acbbcc"
findnoofways(s)