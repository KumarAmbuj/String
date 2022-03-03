def findreverse(s):
    if len(s)==0:
        return

    a=s[0]
    findreverse(s[1:])
    print(a,end='')

findreverse('geeksforgeeks')