def check(s):
    ones=0
    zeros=0
    for i in range(len(s)):
        if s[i]=='1':
            ones+=1
        elif s[i]=='0':
            zeros+=1
    return ones>=zeros

def find(s,n,ones,zeros):
    if len(s)>=n:

        print(s,end=' ')
        return

    find(s+'1',n,ones+1,zeros)

    if ones>zeros:
        find(s+'0',n,ones,zeros+1)

def printallhavingmoreones(n):
    res=''
    ones=0
    zeros=0
    find(res,n,ones,zeros)
printallhavingmoreones(2)
print()
printallhavingmoreones(3)
print()
printallhavingmoreones(4)
print()
printallhavingmoreones(5)