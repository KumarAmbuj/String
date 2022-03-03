def removespace(s):
    res=''
    for x in s:
        if x==' ':
            continue
        else:
            res=res+x
    print(res)

s="g  eeks   for ge  eeks"
removespace(s)