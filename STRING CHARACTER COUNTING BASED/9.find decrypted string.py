def findDecryptedString(string,k):

    res=''

    i=0
    d=0
    while(i<len(string)):
        prev=''
        d=0
        while(i<len(string) and string[i].isalpha()):
            prev=prev+string[i]
            i+=1
        while(i<len(string) and string[i].isdigit()):
            d=d*10+int(string[i])
            i+=1

        res=res+prev*d

    if d==0:
        res=res+res+prev

    print(res)



    return res[k-1]




s="a2b2c3"
k = 5
print(findDecryptedString(s,k))

s="ab4c12ed3"
k = 21
print(findDecryptedString(s,k))

s="ab4c2ed3"
k = 9
print(findDecryptedString(s,k))

