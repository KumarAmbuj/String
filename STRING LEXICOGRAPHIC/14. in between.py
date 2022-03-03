def findnext(s):
    s=list(s)

    for i in range(len(s)-1,-1,-1):
        if s[i]!='z':
            s[i]=chr(ord(s[i])+1)
            return ''.join(s)
        s[i]='a'
    return ''.join(s)

def findinbetween(s1,s2):
    s=''
    s=findnext(s1)
    #print(s)


    if s:
        if s < s2:
            print(s)
        else:
            print(-1)
    else:
        print(-1)


findinbetween('azz','ccc')