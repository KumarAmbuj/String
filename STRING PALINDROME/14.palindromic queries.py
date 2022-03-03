def ispalindrome(s,low,high):
    while(low<high):
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True


def palindromicQueries(arr,s):
    for i in range(len(arr)):
        low=arr[i][0]
        high=arr[i][1]
        if ispalindrome(s,low,high):
            print(arr[i],'is palindrome')
        else:
            print(arr[i],'is not a palindrome')

arr=[[0,10],[5,8],[2,5],[5,9]]
s='abaaabaaaba'
palindromicQueries(arr,s)
