def findcombination(arr,s,l,path):
    if len(s)==len(arr):
        print(s)
        return

    for i in range(len(arr)):
        if i not in path:
            res=s+arr[i]
            path.append(i)
            findcombination(arr,res,l,path)
            path.pop()

def findallcombinations(arr):

    l=[]
    path=[]
    res=''
    findcombination(arr,res,l,path)

findallcombinations('ABCD')