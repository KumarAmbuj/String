def checkAnagram(s1,s2):
    dic={}

    for x in s1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in s2:
        if x in dic:
            dic[x]-=1
        else:
            dic[x]=1

    for x in dic:
        if dic[x]!=0:
            return False
    return True

input1 = 'abcd'
input2 = 'cabd'
print(checkAnagram(input1, input2) )