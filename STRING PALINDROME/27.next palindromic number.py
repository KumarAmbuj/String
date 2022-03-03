def Add1(s):

    rev=s[::-1]
    carry=0
    l=[]
    a=int(rev[0])+1
    b=str(a%10)
    l.append(str(b))
    carry=a//10


    if carry==0:
        for i in range(1,len(rev)):
            l.append(rev[i])
        l=l[::-1]
    if carry!=0:
        for i in range(1,len(rev)):
            a=int(rev[i])+carry
            b=a%10
            carry=a//10
            l.append(str(b))
        l=l[::-1]

    return l



def makepalindromeAdd(s):
    n=len(s)
    res=[]
    if n%2==1:
        res=s[:(n//2)+1]
        arr=['0']*n
    else:
        res=s[:(n//2)]
        arr=['0']*n



    l=Add1(res)


    for i in range(len(l)):
        arr[i]=arr[n-i-1]=l[i]

    print(''.join(arr))

def makepalindromeReplace(s):
    n=len(s)
    if n%2==1:
        i=n//2-1
        while(i>=0):
            s[n-1-i]=s[i]
            i-=1
    else:
        i=n//2-1
        while(i>=0):
            s[n-1-i]=s[i]
            i-=1
    print(''.join(s))




def generatePalindrome(s):
    n=len(s)
    i=-1

    j=-1
    if n%2==0:
        i=n//2-1
        j=i+1
    else:
        i=n//2-1
        j=n//2+1


    while(i>=0 and j<n):
        if s[i]==s[j]:
            i-=1
            j+=1

        elif s[i]<s[j]:
            makepalindromeAdd(s)

            break
        elif s[i]>s[j]:
            makepalindromeReplace(s)

            break
    else:

        return makepalindromeAdd(s)




def allAre9s(s):
    for i in range(len(s)):
        if s[i]!='9':
            return False
    return True



def nextPalindromicNumber(s):

    if allAre9s(s)==True:
        l=['0']*((len(s))+1)

        l[0]=l[-1]='1'

        print(''.join(l))
    else:

        generatePalindrome(s)






num = [1,1,3,1]
num=list(map(str,num))
nextPalindromicNumber(num)

num = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
num=list(map(str,num))
nextPalindromicNumber(num)

num = [9, 4, 1, 8, 7, 9, 7, 8, 1, 4, 9]
num=list(map(str,num))
nextPalindromicNumber(num)
