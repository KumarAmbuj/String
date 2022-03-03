def makeanagram(s1,s2):
    hash={}
    for x in s1:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in s2:
        if x in hash:
            hash[x]-=1
        else:
            hash[x]=1

    count=0
    for x in hash:
        if hash[x]!=0:
            count+=1
    print(count)

str1 = "bcadeh"
str2 = "hea"
makeanagram(str1,str2)

str1 = "cddgk"
str2 = "gcd"
makeanagram(str1,str2)

str1 = "bca"
str2 = "abc"
makeanagram(str1,str2)

