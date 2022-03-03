from collections import Counter
def fun(input):
    dict=Counter(input)
    print(dict)
    value=sorted(dict.values(),reverse=True)
    second=value[1]

    for (key, val) in dict.iteritems():
        if val == second:
            print(key)

            return

input = ['aaa','bbb','ccc','bbb','aaa','aaa']
fun(input)