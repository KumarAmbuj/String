def checkKanagram(s1,s2,k):

    if len(s1)!=len(s2):
        return False

    hash={}

    for x in s1:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in s2:
        if x in hash and hash[x]>0:
            hash[x]-=1

    count=0

    for x in hash:
        if hash[x]!=0:
            count+=1

    if count<=k:
        print('Yes')
    else:
        print('N0')

str1 = "anagram"
str2 = "grammar"
k = 3
checkKanagram(str1,str2,k)

str1 = "geeks"
str2 = "eggkf"
k = 1
checkKanagram(str1,str2,k)