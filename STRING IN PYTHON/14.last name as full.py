def fun(str):
    l=str.split()
    for i in range(len(l)-1):
        print(l[i][0].upper(),end='.')
    s=l[-1]
    p=''
    p=p+s[0].upper()
    for i in range(1,len(s)):
        p=p+s[i]
    print(p)
fun('mohandas karamchand gandhi')
fun('geeks for geeks')