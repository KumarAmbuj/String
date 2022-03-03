from collections import Counter
def fun(str1,str2):
    dict1=Counter(str1)
    dict2=Counter(str2)

    commondict= dict1&dict2

    if len(commondict)==0:
        return -1

    commonchar=list(commondict.elements())
    commonchars=sorted(commonchar)

    for i in range (len(commonchars)):
        print(commonchars[i],end='')



str1 = 'geeks'
str2 = 'forgeeks'
fun(str1,str2)


