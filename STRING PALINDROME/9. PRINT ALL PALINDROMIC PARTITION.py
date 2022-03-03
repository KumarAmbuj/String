def isPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def findallpartition(s,start,curpart,l):
    if start>=len(s):
        x=curpart.copy()
        l.append(x)
        return

    for i in range(start,len(s)):

        if isPalindrome(s,start,i):

            curpart.append(s[start:i+1])

            findallpartition(s,i+1,curpart,l)

            curpart.pop()


def findPalindromicPartition(s):

    l=[]
    curpart=[]

    findallpartition(s,0,curpart,l)


    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=' ')
        print()


s='nitin'
findPalindromicPartition(s)
