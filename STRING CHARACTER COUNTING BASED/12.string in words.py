def countWords(arr,s):
    dic={}
    l=s.split()
    for x in l:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    count=0
    for x in arr:
        if x in dic and dic[x]>0:
            count+=1
            dic[x]-=1
    print(count)

words = ["welcome", "to", "geeks", "portal"]
str = "geeksforgeeks is a computer science portal for geeks"
countWords(words,str)

words = ["Save", "Water", "Save", "Yourself"]
s    = "Save"
countWords(words,s)