def findnequalparts(s,k):
    if len(s)%k!=0:
        print('not possible')
        return

    n=len(s)//k

    l=[]
    prev=''
    count=0
    for x in s:
        prev=prev+x
        count+=1

        if count==n:
            l.append(prev)
            count=0
            prev=''
    for x in l:
        print(x)

s="a_simple_divide_string_quest"
findnequalparts(s,4)

