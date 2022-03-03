def query(s,i,j):
    n=len(s)
    i=i%n
    j=j%n
    if s[i]==s[j]:
        print('Yes')
    else:
        print('No')

X = "geeksforgeeks"
query(X, 0, 8)
query(X, 8, 13)
query(X, 6, 15)