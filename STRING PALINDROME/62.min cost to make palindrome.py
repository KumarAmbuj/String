def makepalindrome(s):
    n=len(s)

    i=-1
    j=-1

    if n%2==1:
        i=n//2-1
        j=n//2+1
    else:
        i=n//2-1
        j=n//2

    cost=0

    while(i>=0 and j<n):
        if s[i]!=s[j]:
            cost = cost + min(ord(s[i]) - ord('a') + 1, ord(s[j]) - ord('a') + 1)

        i-=1
        j+=1
    print(cost)

makepalindrome('abcdef')

makepalindrome('aba')