def findmax(s):
    l=s.split('0')

    ans=0

    for x in l:
        if len(x)>ans:
            ans=len(x)
    return ans

input = '11000111101010111'
print(findmax(input))

def findmax2(s):
    ans=max(map(len,s.split('0')))
    return ans
input = '11000111101010111'
print(findmax(input))

