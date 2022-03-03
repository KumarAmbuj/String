def reverseEquation(s):
    alpha=[]
    opera=[]

    res=''
    for x in s:
        if x.isalnum():
            res=res+x
        elif x=='+' or x=='-' or x=='*' or x=='/':
            alpha.append(res)
            opera.append(x)
            res=''

    if len(res)>0:
        alpha.append(res)

    res=''
    i=len(opera)-1
    j=len(alpha)-1
    while(i>=0):
        res=res+alpha[j]+opera[i]
        i-=1
        j-=1

    res=res+alpha[0]
    print(res)

s = "a+b*c-d/e"
reverseEquation(s)

s='20 - 3 + 5 * 2'
reverseEquation(s)


def reverseEquation1(s):
    res=''
    prev=''
    for i in range(len(s)):
        if s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i]=='/':
            res=s[i]+prev+res
            prev=''
        else:
            prev=prev+s[i]
    if len(prev)>0:
        res=prev+res

    print(res)

s = "a+b*c-d/e"
reverseEquation1(s)

s='20 - 3 + 5 * 2'
reverseEquation1(s)
