def isAnBn(s):
    As=0
    Bs=0

    for i in range(len(s)):
        if s[i]=='a':
            As+=1
        if s[i]=='b':
            Bs+=1

    if As!=Bs:
        return False

    if s.rfind('ba')==(len(s)-2):
        return False

    return True


s1 = "aabb"
print(isAnBn(s1))

s2 = "abab"
print(isAnBn(s2))

s3 = "aabbb"
print(isAnBn(s3))

s3 = "ba"
print(isAnBn(s3))

