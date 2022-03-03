def findcomplement(s):
    arr=list(s)
    ones=''
    for i in range(len(arr)):
        if arr[i]=='0':
            ones=ones+'1'
        else:
            ones+='0'
    print('ones complement',*ones)
    #for twos complement

    twos=ones[::-1]
    twos=list(twos)


    if twos[0]=='0':
        twos[0]='1'
        twos=twos[::-1]
        print(*twos)
    else:
        res='0'
        carry=1

        for i in range(1,len(twos)):

            a=int(twos[i])+carry

            if a==2:
                res=res+'0'
                carry=1
            elif a==1:
                res=res+'1'
                carry=0
            elif a==0:
                res=res+'0'
                carry=0
        if carry!=0:
            res=res+'1'
        res=res[::-1]
        print('twos complement',res)

s='11000'
findcomplement(s)



