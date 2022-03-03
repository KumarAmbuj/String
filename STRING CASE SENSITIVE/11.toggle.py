def findtoggle(s):
    for x in s:
        a=ord(x)
        for i in range(6):
            a=a>>1

