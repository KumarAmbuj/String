def fun(string):
    alpha='abcdefghijklmnopqrstuvwxyz'
    list=[]
    for x in alpha:
        if x not in string:
            list.append(x)
    print(list)
fun("The quick brown fox jumps "
                 "over the dog")