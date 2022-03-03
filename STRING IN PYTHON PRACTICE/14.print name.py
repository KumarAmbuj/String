def findname(s):
    ans=''
    l=s.split()

    for i in range(len(l)-1):
        ans=ans+l[i][0].upper()+'.'

    s=l[-1]
    ans=ans+s[0].upper()+s[1:]

    return ans

s='mohandas karamchand gandhi'
print(findname(s))