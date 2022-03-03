def findSubstringContainingKones(s,k):

    count=0

    for i in range(len(s)):
        dic={}

        for j in range(i,len(s)):
            if s[j] in dic:
                dic[s[j]]+=1
            else:
                dic[s[j]]=1


            if '1' in dic and dic['1']==k:
                count+=1

            if '1' in dic and  dic['1']>k:
                break
    print(count)

s = "10010"
K = 1

findSubstringContainingKones(s,K)