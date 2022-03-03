def countSubstr(s,i,j,n):
    if n==1:
        return 1
    if n==0:
        return 0

    res=countSubstr(s,i+1,j,n-1)+countSubstr(s,i,j-1,n-1)-countSubstr(s,i+1,j-1,n-2)

    if s[i]==s[j]:
        res+=1
    return res


def findsubstring(s):
    n=len(s)
    print(countSubstr(s,0,n-1,n))

str = "abcab"
n = len(str)
findsubstring(str)

str = "aaa"
n = len(str)
findsubstring(str)