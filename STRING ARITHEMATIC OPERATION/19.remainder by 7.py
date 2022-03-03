def findremainder(s):
    s=s[::-1]
    a=[1,3,2,-1,-3,-2]

    if len(s)<len(a):
        n=len(s)
    else:
        n=len(a)

    i=0
    res=0
    while(i<n):
        res=res+int(s[i])*a[i]
        i+=1
    return res%7
num = '1234'
print(findremainder(num))

num = '12345678'
print(findremainder(num))

print(12345678%7)
