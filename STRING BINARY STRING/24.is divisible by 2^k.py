def isdivisible(s,k):

    c=0
    n=len(s)

    for i in range(k):
        if s[n-1-i]=='0':
            c+=1

    return c==k

print(isdivisible('11000',2))
print(isdivisible('10101',3))

