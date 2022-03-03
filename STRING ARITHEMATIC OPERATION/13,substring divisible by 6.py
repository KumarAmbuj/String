def findsubstring(s,index,path,l):
    if index>=len(s):
        l.append(''.join(path))
        return

    path.append(s[index])

    findsubstring(s,index+1,path,l)

    path.pop()
    findsubstring(s,index+1,path,l)


def isDivisible(s):

    l=[]
    path=[]

    findsubstring(s,0,path,l)

    count=0

    for x in l:
        if len(x)>0:

            if int(x)%6==0:
                count+=1
    return count

s = "4806"
print(isDivisible(s))

s='6564525600'
print(isDivisible(s))
