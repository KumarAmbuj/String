def fun(str):
    list=str.split()
    max=0
    min=345
    maxword=''
    minword=''
    for x in list:
        if len(x)>max:
            max=len(x)
            maxword=x
        elif len(x)<min:
            min=len(x)
            minword=x
    print(maxword)
    print(minword)

fun("GeeksforGeeks A computer Science portal for Geeks")