def countSubstring(s):
    res=''
    count=0

    for i in range(len(s)):
        res=''
        for j in range(i,len(s)):
            res=res+s[j]
            if res[0]==res[-1]:
                count+=1
    print(count)
S = "abcab"
countSubstring(S)

S = "aba"
countSubstring(S)