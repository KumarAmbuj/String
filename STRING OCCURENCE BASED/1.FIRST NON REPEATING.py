def findfirst(s):
    hash={}
    for x in s:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1
    for x in hash:
        if hash[x]==1:
            print(x)
            break
    else:
        print('not found')

s='geeksforgeeks'
findfirst(s)