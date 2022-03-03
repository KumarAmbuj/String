def findSmallestWindow(string,pat):
    len1=len(string)
    len2=len(pat)

    dic1=[0]*256
    dic2=[0]*256

    for x in pat:
        dic2[ord(x)]+=1


    start=0
    startindex=-1
    minlen=99
    count=0

    for j in range(len(string)):

        dic1[ord(string[j])]+=1

        if dic2[ord(string[j])]!=0 and \
            dic1[ord(string[j])]<= \
            dic2[ord(string[j])]:
            count+=1

        if count==len2:

            while((dic1[ord(string[start])]> \
                  dic2[ord(string[start])]) or \
                  dic2[ord(string[start])] ==0):

                if dic1[ord(string[start])] > dic2[ord(string[start])]:
                    dic1[ord(string[start])]-=1
                start+=1

            windowlen=j-start+1

            if minlen>windowlen:
                minlen=windowlen
                startindex=start
    if startindex==-1:
        print('not possible')
        return ""

    return string[startindex:startindex+minlen]


string = "this is a test string"
pat = "tist"

print("Smallest window is : ")
print(findSmallestWindow(string, pat))











