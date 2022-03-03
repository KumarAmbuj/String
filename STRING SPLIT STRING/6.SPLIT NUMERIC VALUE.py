def splitting(s,beg,n1,n):

    s1=s[beg:beg+n1]
    s2=str(int(s1)+1)
    n2=len(s2)

    if len(s2)>(n-len(s1)-beg):
        return False

    if s2==s[beg+n1:beg+n1+n2]:

        if beg+n1+n2==n:
            return True

        return splitting(s,beg+n1,n2,n)
    return False





def splittingNumeric(s):
    if s[0]=='0':
        print('not possible')
        return
    n=len(s)
    for i in range(1,(len(s)//2)+1):
        if splitting(s,0,i,n):
            res=s[:i]
            print('yes',res)
            break
    else:
        print('not possible')

splittingNumeric('1234')
splittingNumeric('99100')
splittingNumeric('99101')
splittingNumeric('99100101102')



