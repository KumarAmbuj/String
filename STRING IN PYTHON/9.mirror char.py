def fun(str,n):
    a='abcdefghijklmnopqrstuvwxyz'
    b='zyxwvutsrqponmlkjihgfedcba'
    s=''
    for i in range(n-1):
        s=s+str[i]
    for i in range(n-1,len(str)):
        for j in range(len(a)):
            if str[i]==a[j]:
                s=s+b[j]
    print(s)
fun('pneumonia',6)
