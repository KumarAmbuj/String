def findDiff(s1,s2):
    if len(s2)>len(s1):
        s1,s2=s2,s1
    n1=len(s1)
    n2=len(s2)
    n=n1-n2

    s2='0'*n+s2

    s1=s1[::-1]
    s2=s2[::-1]

    res=''
    i=0
    borrow=0
    while(i<n1):
        sub=int(s1[i])-int(s2[i])-borrow

        if sub<0:
            sub=sub+10
            borrow=1
        else:
            borrow=0

        res=res+str(sub)
        i+=1
    res=res[::-1]

    return res





str1 = "11443333311111111100"
str2 =  "1144422222221111"
print(findDiff(str1,str2))

str1 = "122387876566565674"
str2 =     "31435454654554"

print(findDiff(str1,str2))
