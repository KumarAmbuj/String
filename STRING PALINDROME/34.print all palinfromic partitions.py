def isPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def findpartitions(s,start,currpart,allpart,n):
    if start>=n:
        x=currpart.copy()

        allpart.append(x)

        return

    for i in range(start,n):

        if isPalindrome(s,start,i):
            currpart.append(s[start:i+1])

            findpartitions(s,i+1,currpart,allpart,n)

            currpart.pop()



def findAllPartitions(s):
    currpart=[]
    allpart=[]

    findpartitions(s,0,currpart,allpart,len(s))



    for i in range(len(allpart)):
        for j in range(len(allpart[i])):
            print(allpart[i][j],end=' ')
        print()

findAllPartitions('nitin')

findAllPartitions('geeks')