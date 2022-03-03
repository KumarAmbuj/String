def Add1(s):
    print(s)
    rev=s[::-1]
    print(rev)
    carry=0
    l=[]
    a=int(rev[0])+1
    b=str(a%10)
    l.append(str(b))
    carry=a//10


    if carry==0:
        for i in range(1,len(rev)):
            l.append(rev[i])
        l=l[::-1]
    if carry!=0:
        for i in range(1,len(rev)):
            a=int(rev[i])+carry
            b=a%10
            carry=a//10
            l.append(str(b))
        l=l[::-1]

    print(l)

Add1(['1','9'])
