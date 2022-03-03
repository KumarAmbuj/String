def findlexicomax(s):
    index=0
    mx=s[0]

    for i in range(1,len(s)):
        if ord(s[i])>ord(mx):
            index=i
            mx=s[i]
    res=s[index:]
    print(res)
findlexicomax('ababaa')
findlexicomax('asdfaa')
