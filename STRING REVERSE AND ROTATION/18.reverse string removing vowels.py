def findreverse(s):
    n=len(s)
    for i in range(n):
        r=s[n-i-1]

        if s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u':
            print(r,end='')

s = "geeksforgeeks"
findreverse(s)