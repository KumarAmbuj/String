def reverse1(s):
    s=''.join(reversed(s))
    return s
print(reverse1('Geeksforgeeks'))

def reverse2(s):
    ans=''
    for x in s:
        ans=x+ans
    return ans
print(reverse2('Geeksforgeeks'))

def reverse3(s):
    ans=s[::-1]
    return ans
print(reverse3('Geeksforgeeks'))

def reverse4(s):
    if len(s)==0:
        return s

    else:
        return reverse4(s[1:])+s[0]


print(reverse4('Geeksforgeeks'))







