def findSum(s1,s2):
    s1=str(s1)
    s2=str(s2)
    if len(s2)>len(s1):
        s1,s2=s2,s1

    n1=len(s1)
    n2=len(s2)

    n=n1-n2

    s2=('0'*n)+s2

    res=''
    s1=s1[::-1]
    s2=s2[::-1]


    i=0
    carry=0
    while(i<n1):
        a=int(s1[i])+int(s2[i])+carry
        res=res+str(a%10)
        carry=a//10
        i+=1
    if carry>0:
        res=res+str(carry)

    res=res[::-1]

    print(res)

str1 = "3333311111111111"
str2 =   "44422222221111"
findSum(str1,str2)

str1 = "7777555511111111"
str2 =    "3332222221111"
findSum(str1,str2)

