def findstring(s):
    char=[0]*26

    for x in s:
        char[ord(x)-ord('a')]+=1

    one=''
    many=''

    for i in range(len(char)):
        if char[i]==1:
            one=one+chr(i+ord('a'))
        elif char[i]>1:
            many=many+chr(i+ord('a'))
    print(one)
    print(many)

s='geeksforgeeks'
findstring(s)

s='geekspractice'
findstring(s)

s='lovetocode'
findstring(s)