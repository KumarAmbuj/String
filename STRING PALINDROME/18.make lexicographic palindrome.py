def makepalindrome(s):
    char=[0]*26
    hash={}

    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1


        char[ord(x)-ord('a')]+=1

    k=''
    odd=0
    for x in hash:
        if hash[x]%2==1:
            odd+=1
            k=x
    if odd>1:
        print('not possible')
        return

    palin=['']*len(s)

    if k!='':
        palin[len(s)//2]=k
        char[ord(k)-ord('a')]-=1

    low=0
    high=len(palin)-1
    n=len(palin)
    for i in range(len(char)):
        if char[i]!=0:

            k=char[i]//2


            for m in range(k):
                palin[low]=palin[high]=chr(i+ord('a'))
                low+=1
                high-=1
            char[i]=0
    print(''.join(palin))

makepalindrome('malayalam')
makepalindrome('apple')

makepalindrome('bbccaaaaaccbb')




