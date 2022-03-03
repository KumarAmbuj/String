def generate(s):
    dic={}
    for x in s:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    one=[]
    many=[]

    for x in dic:
        if dic[x]==1:
            one.append(x)
        elif dic[x]>1:
            many.append(x)

    print('only once:',''.join(one))
    print('more than once:',''.join(many))

str = "geeksforgeeks"
generate(str)