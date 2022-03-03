def makeequal(s):
    ones=0
    zeros=0

    for i in range(len(s)):
        if s[i]=='0':
            ones+=1
        else:
            zeros+=1
    return (ones==1 or zeros==1)
s='101'
print(makeequal(s))

s='11'
print(makeequal(s))