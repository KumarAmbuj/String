def isRotation(s,r):
    if s==r:
        return True

    for i in range(1,len(s)):
        res=s[i:]+s[:i]
        if res==r:
            return True
    return False

s='ABACD'
r='CDABA'
print(isRotation(s,r))