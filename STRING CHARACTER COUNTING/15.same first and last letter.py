def fun(str):
    l=[]
    for i in range(len(str)):
        temp=''
        for j in range(i,len(str)):
            temp=temp+str[j]
            l.append(temp)
    print(l)
    result=0
    for x in l:
        if x[0]==x[-1]:
            result=result+1
    print(result)

fun('abcab')