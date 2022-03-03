def fun(str):
    l=str.split('.')
    list=[]
    for x in l:
        x=x.lstrip('0')

        list.append(x)
    s='.'
    s='.'.join(list)
    print(s)
ip ="100.020.003.400"
fun(ip)
ip ="001.200.001.004"
fun(ip)

