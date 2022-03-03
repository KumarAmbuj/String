def fun(str,substr):
    l=str.split()
    for x in l:
        if x==substr:
            print('Yes')
            break
    else:
        print('not')
s1 = 'geeks'
s2='geeks for geeks'
fun(s2,s1)

def fun2(str,substr):
    if str.find(substr)==-1:
        print('No')
    else:
        print('Yes')
fun2(s2,s1)