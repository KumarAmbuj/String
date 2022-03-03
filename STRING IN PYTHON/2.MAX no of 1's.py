def fun(str):
    print(max(map(len,str.split('0'))))
fun('11000111101010111')

def fun1(str):
    max=0
    count=1
    for i in range(len(str)-1):

        if str[i]==str[i+1]:
            count=count+1
            if count>max:
                max=count
        else:
            count=1

    print(max)
fun1('11000111101010111')



