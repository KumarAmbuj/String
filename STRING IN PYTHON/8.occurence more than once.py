from collections import Counter
def fun(str):
    dict=Counter(str)
    print('string with characters occuring once')
    for k in dict.keys():
        if dict.get(k)==1:
            print(k,end='')
    print()

    print('string with characters occuring mutiple times')
    for k in dict.keys():
        if dict.get(k)>1:
            print(k,end='')


fun('geekspractice')
