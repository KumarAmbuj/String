def reverseVowels(s):
    l=list(s)

    i=0
    j=len(l)-1
    vowels=['a','e','i','o','u']

    while(i<j):
        while(l[i] not in vowels):
            i+=1
        while(l[j] not in vowels):
            j-=1
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
    print(''.join(l))

s='hello world'
reverseVowels(s)