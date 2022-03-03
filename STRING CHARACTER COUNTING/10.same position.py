def fun(str):
    result=0
    for i in range(len(str)):
        if (i==ord(str[i])-ord('a')) or i== (ord(str[i])-ord('A')):
            result=result+1
    print(result)

fun('AbgdeF')