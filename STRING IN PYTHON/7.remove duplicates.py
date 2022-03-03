def fun(str):
    s=str[0]
    i=1
    while i <len(str):
        if str[i]==s[-1]:
            i=i+1
        else:
            s=s+str[i]
    print(s)


fun('geeksforgeeks')
