def moveSpaceToFront(s):
    a=" "
    count=0
    for x in s:
        if x==' ':
            count+=1

    l=s.split(' ')
    res=''
    res=res+(' '*count)+''.join(l)
    return res
s="geeks for geeks"
print(moveSpaceToFront(s))

s="geeks for  geeks"
print(moveSpaceToFront(s))

def moveSpaceToFront1(s):
    l=[ch for ch in s if ch!=' ']

    count=len(s)-len(l)

    res=' '*count+''.join(l)

    return res
input = 'geeks for geeks'
print(moveSpaceToFront1(input))

