def Add(s1,s2):
    if len(s2)>len(s1):
        s1,s2=s2,s1
    n1=len(s1)
    n2=len(s2)
    n=n1-n2
    s2=s2+'0'*n
    carry=0

    res=''

    i=0
    while(i<n1):

        a=int(s1[i])+int(s2[i])+carry
        res=res+str(a%10)
        carry=a//10
        i+=1

    return res




def findproduct(s1,s2):
    if len(s2)>len(s1):
        s1,s2=s2,s1

    s1=s1[::-1]
    s2=s2[::-1]

    res=''

    for i in range(len(s2)):
        s='0'*i
        carry=0

        for j in range(len(s1)):
            a=int(s1[j])*int(s2[i])+carry
            s=s+str(a%10)
            carry=a//10
        if carry!=0:
            s=s+str(carry)
        if len(res)==0:
            res=s
        else:
            res=Add(res,s)

    res=res[::-1]
    print(res)

num1 = '4154'
num2 = '51454'
findproduct(num1,num2)

num1 = '4'
num2 = '14'
findproduct(num1,num2)

num1 = '654154154151454545415415454'
num2 = '63516561563156316545145146514654'
findproduct(num1,num2)
