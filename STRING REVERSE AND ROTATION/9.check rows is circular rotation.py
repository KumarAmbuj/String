def isCircular(arr):
    s=''
    for x in arr[0]:
        s=s+str(x)
    s=s+s

    for i in range(1,len(arr)):
        res=''
        for x in arr[i]:
            res=res+str(x)
        if res not in s:
            return False

    return True

mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
print(isCircular(mat))

mat =[[ 1, 2, 3],
                   [3, 2, 1],
                   [1, 3, 2]]
print(isCircular(mat))


def isCircular1(arr):
    l=arr[0]
    for i in range(1,len(arr)):

        l=l[len(l)-1:]+l[:len(l)-1]

        if l!=arr[i]:
            return False

    return True
mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
print(isCircular1(mat))

mat =[[ 1, 2, 3],
                   [3, 2, 1],
                   [1, 3, 2]]
print(isCircular1(mat))