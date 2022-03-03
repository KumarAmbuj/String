def findpalindrome(s,i,j,start,end,maxlen):
    if i==j:
        return
    if i>j:
        return

    if s[i]==s[j]:
        findpalindrome(s,i+1,j-1,start,end,maxlen)
    else:
        findpalindrome(s,i+1,j,start,end,maxlen)
        findpalindrome(s,i,j-1,start,end,maxlen)

    if s[i]==s[j] and (i-1)>=0 and (j+1)<(len(s)) and  s[i-1]==s[j+1] and (j+1-i+1)>maxlen[0]:
        maxlen[0] = j+1 - i+1
        start[0] = i-1
        end[0] = j+1


def findlongestpalindrome(s):
    res=''
    for x in s:
        if x.isalnum():
            res=res+x

    start=[-1]
    end=[-1]
    maxlen=[-9]

    findpalindrome(res,0,len(s)-1,start,end,maxlen)

    if start[0]!=-1 and end[0]!=-1:
        print(res[start[0]:end[0]+1])
    else:
        print('not found')

findlongestpalindrome("forgeeksskeegfor")
findlongestpalindrome("forgegs")



