def findmin(s):
    index=-1
    mn=s[0]

    for i in range(1,len(s)):
        if ord(s[i])<ord(mn):
            mn=s[i]
            index=i

    res=s[index:]+s[:index]

    print(res)

findmin('gksforgeeks')
findmin('amBuj')