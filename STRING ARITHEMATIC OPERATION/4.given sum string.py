def findSum(s1,s2):
    s=int(s1)+int(s2)
    return str(s)

def checkSumUtil(s,index,len1,len2):

    s1=s[index:index+len1]
    s2=s[index+len1:index+len1+len2]
    s3=findSum(s1,s2)
    len3=len(s3)

    if len(s3)>(len(s)-len(s1)-len(s2)-index):
        return False

    if s3==s[index+len1+len2:index+len1+len2+len3]:
        if index+len1+len2+len3==len(s):
            return True

        return checkSumUtil(s,index+len1,len2,len3)
    return False





def isSumString(s):
    for i in range(1,len(s)):
        for j in range(1,len(s)):
            if checkSumUtil(s,0,i,j):
                return True
    return False

print(isSumString("1212243660"))
print(isSumString("123456787"))
s='1111112223'
print(isSumString(s))