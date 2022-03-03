def isanagram(s1,s2):
    hash={}
    for x in s1:
        if x.isalpha():
            x = x.lower()
            if x in hash:
                hash[x] += 1
            else:
                hash[x] = 1


    for x in s2:
        if x.isalpha():
            x = x.lower()
            if x in hash:
                hash[x] -= 1
            else:
                hash[x] = 1

    for x in hash:
        if hash[x]>0:
            return False
    return True
s1="William Shakespeare"
s2 = "I am a weakish speller"
print(isanagram(s1,s2))

s1="a gentleman"
s2 = "elegant man"
print(isanagram(s1,s2))

s1="geeksforgeeks"
s2 = "GEEKSFORGEEKS"
print(isanagram(s1,s2))

