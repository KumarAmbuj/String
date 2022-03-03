def rev(str):
    s=''
    for i in range(len(str)):
        s=str[i]+s
    print(s)
rev('fio')

def fun(str):
    if len(str)==0:
        return str
    else:
        return fun(str[1:])+str[0]
print(fun('iuytt'))

def fun2(str):
    str=str[::-1]
    print(str)
fun2('sunny')