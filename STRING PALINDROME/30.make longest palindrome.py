def makepalindrome(s):
    beg=''
    mid=''
    end=''

    char=[0]*26

    for i in range(len(s)):
        char[ord(s[i])-ord('a')]+=1

    i=0
    while(i<len(char)):

        if char[i]==0:
            i+=1
            continue
        if char[i] % 2 == 1:

            mid = chr(i + ord('a'))

            char[i] -= 1

        else:

            for k in range(char[i] // 2):
                beg = beg + chr(i + ord('a'))
            i += 1



    end=beg[::-1]
    print(beg)
    print(end)

    res=beg+mid+end
    print(res)

s='abc'
#makepalindrome(s)

s='abcd'
#makepalindrome(s)

s='abbb'
makepalindrome(s)