def Arrange(s):
    vowel='aeiou'

    vo=[]
    cons=[]

    for x in s:
        if x in vowel:
            vo.append(x)
        else:
            cons.append(x)

    vo=sorted(vo)
    cons=sorted(cons)

    if abs(len(vo)-len(cons))>1:
        print('not possible')
        return

    res=''
    if len(vo)>len(cons):
        i=0
        j=0
        while(i<len(vo) and j<len(cons)):
            res=res+vo[i]
            i+=1
            res=res+cons[j]
            j+=1
        res=res+vo[i]
    elif len(cons)>len(vo):
        i=0
        j=0
        while(i<len(cons) and j<len(vo)):
            res=res+cons[i]
            i+=1
            res=res+vo[j]
            j+=1
        res=res+cons[i]

    else:
        i=0
        j=0
        res=''
        if ord(vo[0])>ord(cons[0]):
            while(i<len(vo) and j<len(cons)):
                res=res+vo[i]+cons[j]
                i+=1
                j+=1
        else:
            while (i < len(vo) and j < len(cons)):
                res = res + cons[i] + vo[j]
                i += 1
                j += 1

    print(res)

s='geeks'
Arrange(s)

s='onse'
Arrange(s)


