def findallanagram(arr,s,n):
    if len(s)==n:
        print(s)
        return

    for i in range(n):
        if arr[i] not in s:
            res=s+arr[i]
            findallanagram(arr,res,n)


def findanagram(arr):
    res=''
    findallanagram(arr,res,len(arr))

findanagram('ABC')