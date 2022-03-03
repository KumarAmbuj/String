def removerecurring(s):
    res=''
    prev=''
    for x in s:
        if x==prev:
            continue
        else:
            res=res+x
            prev=x
    print(res)

s="1299888833"
removerecurring(s)

s="1299888833222"
removerecurring(s)