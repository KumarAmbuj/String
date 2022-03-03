def isvalid(s):
    prev=''
    flag=False

    for i in range(len(s)):

        if s[i]=='1' and flag==False:
            prev='1'
            flag=True
        elif s[i]=='0' and flag==True:
            prev=prev+'0'
        elif s[i]=='1' and flag==True and '0' in prev:
            return False
    return True

print(isvalid('1001'))
print(isvalid('10010'))
print(isvalid('010010'))
print(isvalid('0110'))

