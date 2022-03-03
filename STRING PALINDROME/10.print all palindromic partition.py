def isPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def findpalindromicpartition(s,start,curpart,l):
    if start>=len(s):
        x=curpart.copy()
        l.append(x)
        return

    for i in range(start,len(s)):
        if isPalindrome(s,start,i):

            curpart.append(s[start:i+1])

            findpalindromicpartition(s,i+1,curpart,l)

            curpart.pop()


def findAllPalindromicPartition(s):
    l=[]
    curpart=[]

    findpalindromicpartition(s,0,curpart,l)

    print(l)

s='geeks'
findAllPalindromicPartition(s)