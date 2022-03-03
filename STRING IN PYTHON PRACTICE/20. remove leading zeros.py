def removeleadingzeros(s):
    l=s.split('.')

    ans=[]

    for x in l:
        ans.append(x.lstrip('0'))

    print('.'.join(ans))
s='100.020.003.400 '
removeleadingzeros(s)

def removeLeadingZeros1(s):
    l=s.split('.')
    ans=[]

    for x in l:
        i=0

        while(i<len(x)):
            if x[i]=='0':
                i+=1
            else:
                ans.append(x[i:])
                break

    print('.'.join(ans))

s='100.020.003.400'
removeLeadingZeros1(s)
