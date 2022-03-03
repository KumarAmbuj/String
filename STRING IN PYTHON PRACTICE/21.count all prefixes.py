def countallprefixes(s,a1,a2):
    dic={}
    dic[a1]=0
    dic[a2]=0

    pref=''
    count=0
    for x in s:
        pref=pref+x
        if x in dic:
            dic[x]+=1

        if dic[a1]>dic[a2]:
            count+=1
            print(pref)
    print(count)

s='geeksforgeeks'
a1='e'
a2='k'
countallprefixes(s,a1,a2)

s='geek'
a1='e'
a2='k'
countallprefixes(s,a1,a2)

s='geek'
a1='k'
a2='e'
countallprefixes(s,a1,a2)


