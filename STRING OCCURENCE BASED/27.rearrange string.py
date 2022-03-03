def rearrange(s,X,Y):
    zeros=0
    ones=0
    for x in s:
        if x=='0':
            zeros+=1
        if x=='1':
            ones+=1
    res=''
    while(zeros>0 and ones>0):

        if zeros>X:
            res=res+'0'*X
            zeros=zeros-X
        else:
            res=res+'0'*zeros
            zeros=0

        if ones>Y:
            res=res+'1'*Y
            ones=ones-Y
        else:
            res=res+'1'*ones
            ones=0

    if zeros>0:
        res=res+'0'*zeros
    if ones>0:
        res=res+'1'*ones
    print(res)
str1 = "01101101101101101000000"
x = 1
y = 3
rearrange(str1, x, y)