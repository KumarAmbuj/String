def finddifficulty(s):
    l=s.split()
    vowel='aeiouAEIOU'
    dif=0
    easy=0

    for x in l:
        prev=''
        cons = 0
        vow = 0
        ans=0
        for i in x:
            if i not in vowel:
                prev=prev+i
                cons+=1
            else:
                ans=max(ans,len(prev))
                vow+=1
                prev=''
        ans=max(ans,len(prev))

        if ans>=4 or cons>vow:
            dif+=1
        else:
            easy+=1
    res=5*dif+3*easy
    return res
s="Difficulty of sentence"
print(finddifficulty(s))

str = "I am a geek"
print(finddifficulty(str))

str2 = "We are geeks"
print(finddifficulty(str2))




