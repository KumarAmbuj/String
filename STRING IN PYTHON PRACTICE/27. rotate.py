def rotate(s,d):
    left=s[d:]+s[0:d]
    right=s[len(s)-d:]+s[:len(s)-d]

    print(s)
    print(left)
    print(right)

s = "GeeksforGeeks"
d = 2
rotate(s,d)
