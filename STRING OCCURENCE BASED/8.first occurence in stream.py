def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Front(q):
    return q[0]
def Size(q):
    return len(q)


def findfirstoccurrence(s):
    char=[0]*26

    l=[]
    q=Queue()

    for i in range(len(s)):
        x=s[i]

        char[ord(x)-ord('a')]+=1
        Enqueue(q,x)

        a=Front(q)

        if char[ord(a)-ord('a')]==1:
            l.append(a)
        elif char[ord(a)-ord('a')]>1:
            while(Size(q)>0 and Front(q)==a):
                x=Dequeue(q)
            if (Size(q)==0):
                l.append(-1)
    for x in l:
        print(x)



findfirstoccurrence('aabc')
