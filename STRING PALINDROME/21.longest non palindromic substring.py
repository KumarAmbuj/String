def ispalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def findmin(s,i,j):
    if i==j:
        return 0

    k1=0
    k2=0
    if ispalindrome(s,i,j):
        k1=findmin(s,i+1,j)
        k2=findmin(s,i,j-1)


    else:
        return j-i+1

    return max(k1,k2)





def minno(s):
    i=0
    j=len(s)-1
    return findmin(s,i,j)

print(minno('aaa'))

print(minno('aabbaa'))

print(minno('abba'))

print(minno('abcdef'))