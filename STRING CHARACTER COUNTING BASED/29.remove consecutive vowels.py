def removeVowels(s):

    vowels='aeiouAEIOU'

    flag=False
    prev=''
    for x in s:
        if x in vowels and flag==False:
            prev=prev+x
            flag=True
        elif x in vowels and flag==True:
            continue
        elif x not in vowels:
            prev=prev+x
            flag=False

    print(prev)

a='geeks for geeks'
removeVowels(a)


a='your article is in queue'
removeVowels(a)


def removeVowels1(s):
    vowels='aeiouAEIOU'
    res=''
    for x in s:
        if x in vowels and len(res)>0 and res[-1] in vowels:
            continue
        else:
            res=res+x
            
    print(res)

a='geeks for geeks'
removeVowels1(a)


a='your article is in queue'
removeVowels1(a)

