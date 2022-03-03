def removespaces(s):
    l=s.split()
    res=''
    res=l[0]
    for i in range(1,len(l)):
        if l[i]=='.':
            res=res+'.'
        else:
            res=res+' '+l[i]
    print(res)

s="   Hello Geeks . Welcome   to  GeeksforGeeks   .    "
removespaces(s)

s="GeeksforGeeks"
removespaces(s)