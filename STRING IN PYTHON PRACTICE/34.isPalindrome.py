def isPalindrome(s):
    return s==s[::-1]
s = "malayalam"
print(isPalindrome(s))

s = "geeks"
print(isPalindrome(s))


def isPalindrome1(s):
    n=len(s)
    for i in range(len(s)//2):
        if s[i]!=s[n-1-i]:
            return False
    
    return True

s = "malayalam"
print(isPalindrome1(s))

s = "geeks"
print(isPalindrome1(s))
