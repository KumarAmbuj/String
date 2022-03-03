def findcommon(s1,s2):
    dic={}

    for x in s1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    print(dic)
    for x in s2:
        if x in dic and dic[x]>0:
            print(x,end='')
            dic[x]-=1
    print()
str1 = 'geeks'
str2 = 'forgeeks'
findcommon(str1, str2)

string1 = 'hhhhhello'
string2 = 'gfghhmh'
findcommon(string1,string2)