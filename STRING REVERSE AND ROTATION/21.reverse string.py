def reversewords(s):
    l=s.split()
    j=len(l)-1
    res=[]
    i=len(l)-1
    while(i>=0):
        res.append(l[i][::-1])
        i-=2

    n=len(l)
    if n%2==0:
        i=0
        while(i<len(l)):
            res.append(l[i])
            i+=2
    else:
        i=1
        while(i<len(l)):
            res.append(l[i])
            i+=2

    print(' '.join(res))

s='Ashish Yadav Abhishek Rajput Sunil Pundir'
reversewords(s)

s='Ashish Yadav Abhishek Rajput Sunil Pundir Prem'
reversewords(s)