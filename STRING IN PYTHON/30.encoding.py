from collections import Counter
def fun(str1):
    dict=Counter(str1)
    output=''
    for k in dict.keys():
        b=str(dict.get(k))
        output=output+k+b
    print(output)


str1 = 'wwwwaaadexxxxxx'
fun(str1)
