def minflips(s):
    prev=''
    res=0
    for i in range(len(s)):

        if s[i]!=prev:
            res=res+1
        prev=s[i]
    print(res//2)
s='00011110001110'
minflips(s)
