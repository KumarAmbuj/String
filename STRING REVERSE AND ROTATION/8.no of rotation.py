def noOfRotation(s):
    if len(s)==1:
        if int(s)%4==0:
            return 1

    count=0


    for i in range(len(s)):
        res=s[len(s)-i:]+s[:len(s)-i]
        a=int(res[-2])*10+int(res[-1])
        if a%4==0:

            count+=1
    return count

s='43292816'
print(noOfRotation(s))

s='4834'
print(noOfRotation(s))