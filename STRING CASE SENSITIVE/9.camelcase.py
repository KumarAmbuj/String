def camelcase(s):
    prev=''
    res=''
    for x in s:
        if x==' ':
            if len(prev)==1:
                res=res+prev[0].upper()
            else:
                res = res + prev[0].upper() + prev[1:]
            prev = ''

        else:
            prev=prev+x
    if len(prev)>0:
        res=res+prev[0].upper()+prev[1:]
    print(res)
s='I got intern at geeksforgeeks'
camelcase(s)