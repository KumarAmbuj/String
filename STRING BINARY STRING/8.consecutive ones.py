def isconsecutive1s(s):
    for i in range(1,len(s)):
        if s[i]==s[i-1]=='1':
            return True
    return False

def findconsecutiveones(s,n,count):
    if len(s)==n:
        if isconsecutive1s(s):
            count[0]+=1
        return

    res=s+'0'
    findconsecutiveones(res,n,count)

    res=s+'1'
    findconsecutiveones(res, n, count)






def findnoofconsecutiveones(n):
    arr=['0','1']

    count=[0]
    res=''
    findconsecutiveones(res,n,count)
    print(count[0])

findnoofconsecutiveones(2)
findnoofconsecutiveones(4)
findnoofconsecutiveones(5)
