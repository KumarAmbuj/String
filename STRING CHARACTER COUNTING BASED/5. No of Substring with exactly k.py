def findNoofSubstring(string,k):
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

            for x in dic:
                if dic[x]!=k:
                    break
            else:
                count+=1

    return count

s = "aabbcc"
k = 2

print(findNoofSubstring(s,k))


s = "aabccc"
k = 2

print(findNoofSubstring(s,k))
