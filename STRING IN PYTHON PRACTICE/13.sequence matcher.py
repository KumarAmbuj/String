def findmatcher(str1,str2):
    l=[]
    dic={}

    for x in str1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    path=[]

    for x in str2:
        if x in dic and dic[x]>0:
            path.append(x)
            dic[x]-=1
        else:
            l.append(path)
            path=[]

    ans=''
    m=0

    for x in l:
        if len(x)>m:
            m=len(x)
            ans=''.join(x)
    return ans


X = 'dfeGeeksforGeeks'
Y = "acvfdxGeeksQuiz"
print(findmatcher(X,Y))

