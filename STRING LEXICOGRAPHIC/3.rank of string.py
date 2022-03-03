def findpermute(arr,s,word,rank,path,flag,n):
    if flag[0]==True:
        return

    if len(s)==n:
        rank[0]+=1
        if s==word:
            flag[0]=True
        return

    for i in range(len(arr)):
        if i not in path:
            res=s+arr[i]
            path.append(i)
            findpermute(arr,res,word,rank,path,flag,n)
            path.pop()


def findrank(word):
    arr=''.join(sorted(word))
    rank=[0]
    flag=[False]
    n=len(arr)
    path=[]
    res=''
    findpermute(arr,res,word,rank,path,flag,n)
    print(rank[0])

findrank('acb')
findrank('string')
findrank('cba')