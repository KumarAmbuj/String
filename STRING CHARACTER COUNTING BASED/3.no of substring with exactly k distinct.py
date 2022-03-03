def findnoofSubstring(string,k):
    count=0

    for i in range(len(string)):
        prev=''
        for j in range(i,len(string)):
            prev=prev+string[j]

            dic={}

            for x in prev:
                if x in dic:
                    dic[x]+=1
                else:
                    dic[x]=1

            if len(dic)==k:
                count+=1
    return count

s='abc'
k = 2
print(findnoofSubstring(s,k))

s='aba'
k = 2
print(findnoofSubstring(s,k))

s='aa'
k = 1
print(findnoofSubstring(s,k))

