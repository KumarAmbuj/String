from collections import Counter
def fun(str1,str2):
    dict1=Counter(str1)
    dict2=Counter(str2)
    result=dict1&dict2

    return dict1==result
str1 = 'ABHISHEKsinGH'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
if fun(str1,str2)==True:
    print('possible')
else:
    print('not possible')
