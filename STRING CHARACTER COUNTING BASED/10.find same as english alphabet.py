def find(s):
    count=0

    for i in range(len(s)):
        if i==(ord(s[i])-ord('a')) or i==(ord(s[i])-ord('A')):
            count+=1
    print(count)

s='ABcED '
find(s)

s='geeksforgeeks'
find(s)

s='alphabetical'
find(s)