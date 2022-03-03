def ispossible(s):
    hash={}

    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    odd=0
    for x in hash:
        if hash[x]%2==1:
            odd+=1

    if odd==2 or odd==1:
        print(' possible if remove one character')

    elif odd>2:
        print('not possible')

    elif odd==0:
        print('possible without removing a character')

s = 'abcba'
ispossible(s)
