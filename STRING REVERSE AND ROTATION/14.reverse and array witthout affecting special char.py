def findreverse(s):
    l=list(s)
    i=0
    j=len(s)-1

    while(i<j):
        while(l[i].isalnum()==False):
            i+=1
        while(l[j].isalnum()==False):
            j-=1

        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    print(''.join(l))

s = "a,b$c"
findreverse(s)

s = "Ab,c,de!$"
findreverse(s)