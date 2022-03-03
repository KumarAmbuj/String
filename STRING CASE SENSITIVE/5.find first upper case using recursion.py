def find(s):
    if len(s)==0:
        return 0

    if s[0].isupper():
        return s[0]

    return find(s[1:])

def findfirst(s):

    k=find(s)
    if k!=0:
        print(k)
    else:
        print('no uppercase letter')
s='geeksforgeeKs'
findfirst(s)

s='geekS'
findfirst(s)

s='geeks'
findfirst(s)