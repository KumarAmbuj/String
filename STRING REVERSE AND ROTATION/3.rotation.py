def rotation(s,d):
    left=s[d:]+s[:d]
    right=s[len(s)-d:]+s[:len(s)-d]

    print(left)
    print(right)

s = "GeeksforGeeks"
rotation(s,2)