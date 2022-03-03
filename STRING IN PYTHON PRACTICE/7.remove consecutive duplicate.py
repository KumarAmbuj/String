def removeconsecutive(s):
    prev=''
    for  x in s:
        if x==prev:
            continue
        else:
            print(x,end='')
            prev=x
    print()
removeconsecutive('aaaaabbbbbb')
s='geeksforgeeks'
removeconsecutive(s)
removeconsecutive('aabccba')