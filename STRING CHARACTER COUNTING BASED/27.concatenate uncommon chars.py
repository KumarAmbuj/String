def concatuncommon(s1,s2):
    prev=''
    for x in s1:
        if x not in s2:
            prev=prev+x
    for x in s2:
        if x not in s1:
            prev=prev+x
    print(prev)

s1 = "aabcs"
s2 = "cxzc"
concatuncommon(s1,s2)

S1 = "aacdb"
S2 = "gafd"
concatuncommon(S1,S2)