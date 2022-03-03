def findremainder(s):

    quo=''
    rem=''
    i=0
    a=''
    while(i<len(s)):
        a=a+s[i]

        quo=quo+str(int(a)//11)
        rem=str(int(a)%11)
        a=rem
        i+=1
    return rem
s='13589234356546756'
print(findremainder(s))

s='3435346456547566345436457867978'
print(findremainder(s))
