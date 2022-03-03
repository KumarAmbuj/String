def printstring(s,c,count):

    if c not in s:
        print('')
        return
    if count==0:
        print(s)
        return


    for i in range(len(s)):

        if s[i]==c:
            count-=1

        if count==0:
            print(s[i+1:])
            break
    else:
        print('')

s = "This is demo string"
char = 'i'
count = 3
printstring(s,char,count)

s = "geeksforgeeks"
char = 's'
count = 2
printstring(s,char,count)

