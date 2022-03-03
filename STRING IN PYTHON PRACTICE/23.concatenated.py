def concat1(s1,s2):
    pref=''
    for x in s1:
        if x not in s2:
            pref=pref+x

    for x in s2:
        if x not in s1:
            pref=pref+x

    print(pref)

S1 = "aacdb"
S2 = "gafd"
concat1(S1,S2)

S1 = "abcs"
S2 = "cxzca"
concat1(S1,S2)

def concat2(S1,S2):
    dic={}

    for x in S1:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in S2:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    pref=''
    for x in dic:
        if dic[x]==1:
            pref=pref+x

    print(pref)

S1 = "aacdb"
S2 = "gafd"
concat2(S1,S2)

S1 = "abcs"
S2 = "cxzca"
concat2(S1,S2)