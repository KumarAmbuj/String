from collections import Counter

def isPossible(str1,str2):

    s1=Counter(str1)
    s2=Counter(str2)

    result=s1&s2

    if result==s1:
        return True
    else:
        return False

s1 = 'ABHISHEKsinGH'
s2 = 'gfhfBHkooIHnfndSHEKsiAnG'

if isPossible(s1,s2):
    print('possible')
else:
    print('not possible')

s1 = 'Hello'
s2 = 'dnaKfhelddf'
if isPossible(s1,s2):
    print('possible')
else:
    print('not possible')
