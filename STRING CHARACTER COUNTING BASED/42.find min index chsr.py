def findminindexchar(s,pat):

    for x in s:
        if x in pat:
            print(x)
            break
    else:
        print('not possible')

str = "geeksforgeeks"
patt = "set"
findminindexchar(str,patt)




str = "adcffaet"
patt = "onkl"
findminindexchar(str,patt)