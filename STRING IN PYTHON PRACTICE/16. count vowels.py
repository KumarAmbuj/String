def findnoofvowels(s):
    vowels=set('aeiouAEIOU')

    count=0

    for x in s:
        if x in vowels:
            count+=1
    return count

s = "GeeksforGeeks"
print(findnoofvowels(s))