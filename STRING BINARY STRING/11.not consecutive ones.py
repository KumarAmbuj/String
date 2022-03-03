def consec(s):
    for i in range(1,len(s)):
        if s[i]==s[i-1]=='1':
            return False
    return True



def find(s,n,count):
    if len(s)>=n:
        if consec(s):
            count[0]+=1
        return
    res=s+'0'
    find(res,n,count)

    res=s+'1'
    find(res,n,count)


def findnotconsecutiveones(n):
    res=''
    count=[0]
    find(res,n,count)

    print(count[0])
findnotconsecutiveones(2)
findnotconsecutiveones(3)
findnotconsecutiveones(4)
findnotconsecutiveones(5)