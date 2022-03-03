def fun(str1):
    dict={}
    for x in str1:
        if x in dict:
            dict[x]=dict[x]+1
        else:
            dict[x]=1
    print(dict)

    for k in dict:
        dict[k]=1
    for k in dict:
        print(k,end='')


fun('geeksforgeeks')