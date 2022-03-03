def isPalindrome(s):
    prev=''
    for x in s:
        if x.isalnum():
            prev=prev+x

    i=0
    j=len(prev)-1

    while(i<j):
        if prev[i]!=prev[j]:
            return False
        i+=1
        j-=1
    return True

print(isPalindrome("abba"))
print(isPalindrome("abbccbba"))
print(isPalindrome("geeks"))
