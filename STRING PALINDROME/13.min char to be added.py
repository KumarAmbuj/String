def ispalindrome(s):
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True


def minchartoadd(s):
    count=0

    while(True):

        if ispalindrome(s)==False:
            s=s[:len(s)-1]
            count+=1
        else:
            print(count)
            break

minchartoadd("ABC")

minchartoadd("AACECAAAA")