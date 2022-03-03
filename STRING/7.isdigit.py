def fun(st):
    for i in range(len(st)):
        if st[i].isdigit()!=True:
            return False
    return True
str='6790'
if fun(str):
    print('integer')
else:
    print('string')