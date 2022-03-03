from collections import Counter
def fun(str):
    n=len(str)
    if n%2==0:
        first = str[0:n // 2]
        second=str[n//2:]
    else:
        first=str[0:n//2]
        second=str[(n//2)+1:]

    if Counter(first)==Counter(second):
        print('Yes')
    else:
        print('No')
str='abccba'
fun(str)

