def fillblanksutil(arr,i,n):
    if i>=n:
        print(*arr)
        return

    if arr[i]!='0' and arr[i]!='1':
        arr[i]='0'

        fillblanksutil(arr,i+1,n)

        arr[i]='1'

        fillblanksutil(arr,i+1,n)

        arr[i]='?'
    else:
        fillblanksutil(arr,i+1,n)




def fillinblanks(s):

    arr=list(s)
    n=len(arr)

    fillblanksutil(arr,0,n)


string = "1??0?101"
fillinblanks(string)