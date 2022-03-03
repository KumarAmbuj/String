def findNoofWords(s):
    prev=''
    count=0
    i=0
    while(i<len(s)):
        if (s[i]==' ' or s[i]=='\n' or s[i]=='\t') and prev.isalpha():
            count+=1
        prev=s[i]
        i+=1

    if prev.isalpha():
        count+=1

    print(count)

s = "One two		 three\n four\tfive "
findNoofWords(s)

s = "One two		 three\n four\tfive six"
findNoofWords(s)