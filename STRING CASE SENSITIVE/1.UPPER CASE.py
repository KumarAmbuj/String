def finduppercase(s):
    arr='abcdefghijklmnopqrstuvwxyz'

    res=''
    for x in s:
        if x in arr:
            a=chr(ord(x)-ord('a')+ord('A'))
            res=res+a
        else:
            res=res+x
    print(res)
s='geeksforgeeks'
finduppercase(s)

s='GeeksForGeeks'
finduppercase(s)