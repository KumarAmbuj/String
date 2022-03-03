def sortstring(arr):

    arr=map(str,arr)
    res=[]

    for x in arr:
        if '1' in x and '2' in x and '3' in x:
            res.append(x)

    res=sorted(res)
    print(' '.join(res))

numbers = [321, 1232, 456,
           234, 32145]
sortstring(numbers)



