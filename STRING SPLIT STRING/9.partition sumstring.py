def findstring(s,beg,len1,len2,l,n):
    s1=s[beg:beg+len1]
    s2=s[beg+len1:beg+len1+len2]

    s3=str(int(s1)+int(s2))
    n3=len(s3)

    if n3>(n-beg-len1-len2):
        return False

    if s3==s[beg+len1+len2:beg+len1+len2+n3]:
        l.append(s1)
        if beg+len1+len2+n3==n:
            l.append(s2)
            l.append(s3)
            return True
        return findstring(s,beg+len1,len2,n3,l,n)



def ispossible(s):
    n=len(s)
    for i in range(1,n):
        for j in range(1,n-i):
            l=[]
            if findstring(s,0,i,j,l,n):
                print(l)
                return
    print('not possible')
    return

s="11235813"
ispossible(s)

s='1111223'
ispossible(s)

s="11121114"
ispossible(s)