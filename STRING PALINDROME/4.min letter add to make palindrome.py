def toMakePalindrome(s):
    hash={}

    for x in s:
        if x.isalnum():
            if x in hash:
                hash[x]+=1
            else:
                hash[x]=1
    odd=0

    for x in hash:
        if hash[x]%2==1:
            odd+=1

    if odd>0:
        return odd-1
    else:
        return odd

s='ab'
print(toMakePalindrome(s))

s='aa'
print(toMakePalindrome(s))

s='abcd'
print(toMakePalindrome(s))

s='abcda'
print(toMakePalindrome(s))

s='abcde'
print(toMakePalindrome(s))






