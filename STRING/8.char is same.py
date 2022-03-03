def fun(st):
    for i in range(1,len(st)):
        if st[i]!=st[0]:
            return False
    return True
str = "aaa"
if fun(str):
    print('yes')
else:
    print('no')