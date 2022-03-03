def movespace(s):
    res=''
    count=0
    for x in s:
        if x==' ':
            count+=1
        else:
            res=res+x
    print(count)
    res=' '*count+res
    print(res)
s = "geeks for geeks"
movespace(s)

s = "move these spaces to beginning "
movespace(s)