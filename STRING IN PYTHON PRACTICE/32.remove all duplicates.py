def removeAllDuplicates(s):
    st=set(s)
    print('without order',''.join(st))

    dic={}

    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    s=dic.keys()

    print(''.join(s))
s='geeksforgeeks'
removeAllDuplicates(s)