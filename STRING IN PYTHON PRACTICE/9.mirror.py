def findmirror(s,n):
    ans=s[:n-1]

    ans1=[]

    for i in range(n-1,len(s)):
        a=ord(s[i])-ord('a')
        b=26-a
        ans1.append(chr(b+ord('a')-1))

    ans=ans+''.join(ans1)
    return ans
N = 3
s='paradox'
print(findmirror(s,N))
N = 6
s='pneumonias'
print(findmirror(s,N))