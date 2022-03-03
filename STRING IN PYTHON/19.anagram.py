def fun(str1,str2):
    if sorted(str1)==sorted(str2):
        print('Anagram')
    else:
        print('not Anagram')
s1 ="listen"
s2 ="silent"
fun(s1,s2)