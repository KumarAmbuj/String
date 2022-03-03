def fun(str):
    a='qwertyuiopasdfghjklzxcvbnm'
    b='abcdefghijklmnopqrstuvwxyz'
    s=''
    for i in range(len(str)):

        for j in range(len(a)):
            if str[i]==a[j]:
                s=s+b[j]
    print(s)
fun('egrt')
