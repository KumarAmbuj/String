def findsmallest(s):
    arr=['a','b','c']
    i=0
    prev=''
    while(i<len(s)):
        if s[i] not in prev:
            prev=prev+s[i]
            i+=1
        elif s[i] in prev:
            prev=s[i]
            i+=1

        if len(prev)==2:
            for x in arr:
                if x not in prev:
                    s=s.replace(prev,x,1)

                    i=0
                    prev=''
                    break

    print(len(s))
findsmallest('bcab')

findsmallest('cab')

findsmallest('abcbbaacb')





