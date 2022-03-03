def fun(str1,str2):
    str1=set(str1)
    str2=set(str2)

    common=str1&str2

    result=[ch for ch in str1 if ch not in common]+[ch for ch in str2 if ch not in common]
    print(''.join(result))
str1 = 'aacdb'
str2 = 'gafd'
fun(str1,str2)