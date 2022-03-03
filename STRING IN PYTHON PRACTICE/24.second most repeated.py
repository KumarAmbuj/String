def secondmostrepeated(l):
    dic={}
    for x in l:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    first=-99
    second=-99
    ans=''

    for x in dic:
        if dic[x]>first:
            second=first
            first=dic[x]
        elif dic[x]>second:
            ans=x
            second=dic[x]
    print(ans)

input = ['aaa','bbb','ccc','bbb','aaa','aaa']
secondmostrepeated(input)

