def istogether(s,c):
    prev=''
    flag=False

    for x in s:
        if x==c and flag==False and len(prev)==0:
            prev=prev+x
            flag=True
        elif x==c and flag==False and len(prev)!=0:
            return False

        if x!=c:
            flag=False

    return True

s = "1110000323"
c = '1'
print(istogether(s,c))

s = "3231131"
c = '1'
print(istogether(s,c))

s = "ababcc"
c = 'c'
print(istogether(s,c))

s = "abaxbcc"
c = 'x'
print(istogether(s,c))
