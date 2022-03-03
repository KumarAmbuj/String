def fun(str1,str2):
    dict={}
    for i in str2:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1

    for j in str1:
        if  j in dict:
            dict[j]=dict[j]-1

    for h in dict:
        if dict[h]==1:
            print(h)
fun('abcd','bcdea')