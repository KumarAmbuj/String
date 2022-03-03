def finduncommonwords(s1,s2):
    hash={}
    s1=set(s1)
    s2=set(s2)

    for x in s1:
        hash[x]=1
    for x in s2:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in hash:
        if hash[x]==1:
            print(x,end=' ')
    print()

str1 = "characters"
str2 = "alphabets"

finduncommonwords(str1,str2)


def finduncommonwords1(s1,s2):
    hash={}

    for x in s1:
        if x not in hash:
            hash[x]=1

    prev=''
    for x in s2:
        if x in hash and x not in prev:
            hash[x]-=1
        elif x not in hash and x not in prev:
            hash[x]=1
        
        prev=prev+x
    for x in hash:
        if hash[x]==1:
            print(x,end=' ')
    print()

str1 = "characters"
str2 = "alphabets"

finduncommonwords1(str1,str2)

