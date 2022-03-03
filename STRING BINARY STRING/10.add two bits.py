def Add(s1,s2):

    if len(s1)>len(s2):
        s2='0'*(len(s1)-len(s2))+s2
    elif len(s2)>len(s1):
        s1='0'*(len(s2)-len(s1))+s1

    
    s1=s1[::-1]
    s2=s2[::-1]

    res=''

    carry=0

    for i in range(len(s1)):
        a=int(s1[i])+int(s2[i])+carry

        if a==2:
            res=res+'0'
            carry=1
        else:
            res=res+str(a)
            carry=0

    if carry!=0:
        res=res+str(carry)

    res=res[::-1]
    print(res)

s1 = '1100011'
s2 = '10'
Add(s1,s2)