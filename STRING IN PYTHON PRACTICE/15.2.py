def isPossible(str1,str2):
    dic={}
    for x in str2:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for x in str1:
        if x in dic and dic[x]>0:
            dic[x]-=1
        else:
            return False

    return True

s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

if isPossible(s1,s2):
    print('possible')
else:
    print('not possible')

s1 = 'Hello'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

if isPossible(s1,s2):
    print('possible')
else:
    print('not possible')
