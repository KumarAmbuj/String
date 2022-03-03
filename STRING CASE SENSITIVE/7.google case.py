def findgooglecase(s):
    res=''
    prev=''

    for x in s:
        if x!=' ':
            prev=prev+x
        else:
            if len(prev)==1:
                res=res+prev[0].lower()+' '

            else:
                res=res+prev[0].lower()+prev[1:].upper()+' '
            prev=''
    if len(prev)>0:
        if len(prev)==1:
            res=res+prev[0].lower()
        else:
            res=res+prev[0].lower()+prev[1:].upper()

    print(res)



s='I got intern at geeksforgeeks'
findgooglecase(s)


