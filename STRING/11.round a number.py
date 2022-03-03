def fun(n):
    if n%10<=5:
        n=n//10
        n=n*10
    else:
        n=n//10
        n=(n+1)*10
    print(n)
fun(42)
