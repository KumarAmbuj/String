def isRotation(s,r):
    for i in range(1,3):
        res=s[i:]+s[:i]
        if res==r:
            return True

    for i in range(1,3):
        res=s[len(s)-i:]+s[:len(s)-i]
        if res==r:
            return True
    return False

s1 = 'amazon'
s2 = 'azonam'
print(isRotation(s1,s2))

s1 = 'amazon'
s2 = 'onamaz'
print(isRotation(s1,s2))

def isRotation1(s,r):

    if s[2:]+s[:2]==r:
        return True
    elif s[len(s)-2:]+s[:len(s)-2]==r:
        return True
    else:
        return False

s1 = 'amazon'
s2 = 'azonam'
print(isRotation1(s1,s2))

s1 = 'amazon'
s2 = 'zonama'
print(isRotation1(s1,s2))

