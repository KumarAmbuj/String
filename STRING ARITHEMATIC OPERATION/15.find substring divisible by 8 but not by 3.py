def findsubstring(s,i,path,l):
    if i>=len(s):
        l.append(''.join(path))
        return

    path.append(s[i])
    findsubstring(s,i+1,path,l)

    path.pop()
    findsubstring(s,i+1,path,l)

def isdivisible(s):
    l=[]
    path=[]

    findsubstring(s,0,path,l)

    count=0

    for x in l:
        if len(x)>0:
            a=int(x)

            if a%8==0 and a%3!=0:
                print(x)
                count+=1
    return count

s='888'
print(isdivisible(s))

