def swapcase(s):
    res=''
    for x in s:
        if ord(x)>=ord('a') and ord(x)<=ord('z'):
            res=res+chr(ord(x)-ord('a')+ord('A'))
        elif ord(x)>=ord('A') and ord(x)<=ord('Z'):
            res=res+chr(ord(x)-ord('A')+ord('a'))
    print(res)
s='GeeksForGeeks'
swapcase(s)