def replacing(s,c1,c2):
    str=list(map(lambda x:x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2,s))

    return ''.join(str)
str = 'grrksfoegrrks'
c1 = 'e'
c2 = 'r'
print(replacing(str,c1,c2))

str = 'ratul'
c1 = 't'
c2 = 'h'
print(replacing(str,c1,c2))