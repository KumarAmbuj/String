def fill(arr,s,i,n):
    if i==n:
        print(s)
        return

    if arr[i]!='0' and arr[i]!='1':
        res=s+'0'
        fill(arr,res,i+1,n)

        res=s+'1'
        fill(arr,res,i+1,n)
    else:
        res=s+arr[i]
        fill(arr,res,i+1,n)

def fillinblanks(arr):
    res=''
    n=len(arr)
    fill(arr,res,0,n)

s="1??0?101"
fillinblanks(s)