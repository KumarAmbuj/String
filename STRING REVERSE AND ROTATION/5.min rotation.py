def findminRotation(s):
    res=s
    count=0

    while(True):
        res=res[1:]+res[:1]
        count+=1
        if res==s:
            print(count)
            break
s='geeks'
findminRotation(s)

s='abc'
findminRotation(s)