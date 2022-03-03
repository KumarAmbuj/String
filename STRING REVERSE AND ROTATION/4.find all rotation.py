def findallRotation(s):
    l=[]
    l.append(s)
    for i in range(1,len(s)):
        l.append(s[i:]+s[:i])

    for x in l:
        print(x)
S = "geeks"
findallRotation(S)

S = "abc"
findallRotation(S)