def findsubstr(s):
    count=0
    for i in range(len(s)):
        if s[i]=='0':
            continue
        prev=''
        for j in range(i,len(s)):
            prev=prev+s[j]
            if len(prev)>1 and prev[0]==prev[-1]:
                count+=1
    print(count)
st = "00100101"
findsubstr(st)
