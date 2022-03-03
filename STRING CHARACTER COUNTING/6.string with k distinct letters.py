def fun(n,k):
    res=''
    for i in range(k):
        res=res+chr(ord('a')+i)

    for i in range(n-k):
        res=res+chr(ord('a')+i)
    print(res)
fun(5,3)
