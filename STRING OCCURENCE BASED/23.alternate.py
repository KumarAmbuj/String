def printalternate(s):
    hash={}

    res=''

    for x in s:

        if x.upper() in hash:
            hash[x.upper()]+=1
        elif x.lower() in hash:
            hash[x.lower()]+=1
        else:
            hash[x]=1

        if (x.upper() in hash and hash[x.upper()]%2==1) or (x.lower() in hash and hash[x.lower()]%2==1):
            res=res+x
    print(hash)
    print(res)
s='It is a long day Dear'
printalternate(s)

s='Geeks for geeks'
printalternate(s)