def ispresent1(s1,s2):
    return s1 in s2
s1 = 'geeks'
s2='geeks for geeks'
print(ispresent1(s1,s2))

def ispresent2(s1,s2):
    if s2.find(s1)!=-1:
        return True
    else:
        return False

s1 = 'geeks'
s2='geeks for geeks'
print(ispresent2(s1,s2))

def ispresent3(s1,s2):
    if s2.count(s1)>0:
        return True
    return False

s1 = 'geeks'
s2='geeks for geeks'
print(ispresent3(s1,s2))




