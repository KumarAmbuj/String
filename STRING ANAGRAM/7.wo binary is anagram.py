def isanagram(n1,n2):
    arr1=''
    arr2=''

    while(n1>0):
        arr1=str(n1%2)+arr1
        n1=n1//2

    while(n2>0):
        arr2=str(n2%2)+arr2
        n2=n2//2

    if len(arr1)>len(arr2):
        arr2='0'*(len(arr1)-len(arr2))+arr2
    elif len(arr2)>len(arr1):
        arr1='0'*(len(arr2)-len(arr1))

    hash={}

    for x in arr1:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in arr2:
        if x in hash:
            hash[x]-=1
        else:
            hash[x]=1

    for x in hash:
        if hash[x]!=0:
            print('NO')
            return
    print('Yes')

isanagram(8,4)

isanagram(5,4)

