def partition(s,a,b):
    n=len(s)

    a=str(a)
    b=str(b)

    for i in range(len(a),n-len(b)+1):
        s1=s[:i]
        s2=s[i:]

        if int(s1)%int(a)==0 and int(s2)%int(b)==0:
            print(s1,s2)
            break
    else:
        print('not possible')

partition('123',12,3)
partition('1200',12,3)
partition('13512',3,12)

