def isPalindrome(n):

    rev=0
    m=n
    while(n>0):
        rev=rev*10+(n%10)
        n=n//10
    return rev==m

def check(min,max):
    l=[]
    for i in range(min,max+1):
        if isPalindrome(i):
            l.append(i)

    count=0
    for x in l:
        count+=1
        print(x,end=' ')
        if count==10:
            count=0
            print()

check(100,2000)

