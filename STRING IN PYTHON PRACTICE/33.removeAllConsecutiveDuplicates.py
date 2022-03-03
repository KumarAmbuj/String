def RemoveAllConsecutiveDuplicates(s):
    p=''
    pref=''

    for x in s:
        if x==p:
            continue
        else:
            pref=pref+x
            p=x
    print(pref)
s='geeksforgeeks'
RemoveAllConsecutiveDuplicates(s)

s='aaaaaabbbbbb'
RemoveAllConsecutiveDuplicates(s)
