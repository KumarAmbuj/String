def findcombinations(arr,s,n,count):
    if len(s)==n:
        dic={}
        for x in s:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        if 'b' in dic and dic['b']<=1 and 'c' in dic and dic['c']<=2 :
            count[0]+=1
        elif ('b' in dic and dic['b']<=1 and 'c' not in dic):
            count[0]+=1
        elif('c' in dic and dic['c']<=2 and 'b' not in dic):
            count[0]+=1
        elif ('b' not in dic and 'c' not in dic):
            count[0]+=1

        return
    if len(s)>n:
        return

    for i in range(len(arr)):
        res=s+arr[i]
        findcombinations(arr,res,n,count)






def findnoofsubstrings(n):
    arr=['a','b','c']
    s=''
    count=[0]
    findcombinations(arr,s,n,count)
    print(count[0])

findnoofsubstrings(3)
