def findlexicosmalleststring(s,k):

    if k<=0 or k>len(s):
        print('not possible')
        return
    m=k
    i=0
    res=''
    while(k>0):

        j=0
        while(chr(j+ord('a'))==s[i]):
            j+=1
        res=res+chr(j+ord('a'))
        k-=1
        i+=1
    res=res+s[m:]
    print(res)
findlexicosmalleststring('pqrs',2)
findlexicosmalleststring('aps',2)




