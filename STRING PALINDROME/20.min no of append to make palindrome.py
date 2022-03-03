def isPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def findminno(s):
    i=0
    j=len(s)-1

    count=0
    while(isPalindrome(s,i,j))==False:
        count+=1
        i+=1

    print(count)
s = "abede"
findminno(s)

s = "aabb"
findminno(s)