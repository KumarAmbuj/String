def isanagram(s1,s2):
    if len(s1)!=len(s2):
        return False
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
    for x in hash:
        if hash[x]!=0:
            return False
    return True



def findpairofanagram(arr):

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if isanagram(arr[i],arr[j]):
                print(arr[i],'is anagram of ',arr[j])
                break

arr = ["geeksquiz", "geeksforgeeks",
           "abcd", "forgeeksgeeks", "zuiqkeegs"]
findpairofanagram(arr)