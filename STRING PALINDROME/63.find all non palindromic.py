def findnonpalindrome(n):
    s=''

    for i in range(n):
        if (i&2)>1:
            s=s+'b'
        else:
            s=s+'a'

    print(s)
findnonpalindrome(3)

findnonpalindrome(5)

findnonpalindrome(4)
