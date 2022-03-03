def ispalindrome(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True



def ispairpalindrome(arr):

    for i in range(len(arr)):
        res=arr[i]
        for j in range(len(arr)):
            if i==j:
                continue
            s=res+arr[j]

            if ispalindrome(s):
                return True
    return False

arr = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
print(ispairpalindrome(arr))