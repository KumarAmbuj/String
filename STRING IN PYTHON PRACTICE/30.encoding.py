def Encoding(s):
    dic={}
    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    res=''

    for x in dic:
        res=res+x+str(dic[x])
    print(res)

st = 'wwwwaaadexxxxxx'
Encoding(st)
