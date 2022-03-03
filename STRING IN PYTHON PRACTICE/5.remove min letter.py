def findminletter1(s1,s2):
    dic={}
    for x in s1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in s2:
        if x in dic:
            dic[x]-=1

    count=0
    for x in dic:
        if dic[x]>0:
            count+=1
    return count

str1 = "bcadeh"
str2 = "hea"
print(findminletter1(str1,str2))



