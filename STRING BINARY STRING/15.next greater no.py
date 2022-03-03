def findnextgreater(s):

    arr=list(s)

    i=len(s)-1
    while(i>=0):
        if arr[i]=='1':
            arr[i]='0'
            i-=1
            break

        i-=1
    if i==-1:
        print('not possible')
        return

    while(i>=0):
        if arr[i]=='0':
            arr[i]='1'
            break
        i-=1
    if i==-1:
        print('not possible')
    else:
        print(''.join(arr))



findnextgreater('110010')
findnextgreater('111000011100111110')
findnextgreater('111')
findnextgreater('111110')

