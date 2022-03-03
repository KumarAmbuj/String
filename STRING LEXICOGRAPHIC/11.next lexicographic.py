def findnextlexicographicstring(s):
    if s=='':
        print('a')
        return

    i=len(s)-1

    while(i>=0 and s[i]=='z'):
        i-=1

    if i==-1:
        res =s+'a'
        print(res)
        return
    else:
        res=s.replace(s[i],chr(ord(s[i])+1),1)
        print(res)
        return

s = "samez"
findnextlexicographicstring(s)

s = "samzz"
findnextlexicographicstring(s)

s = "sazzz"
findnextlexicographicstring(s)

s = "szzzz"
findnextlexicographicstring(s)

s = "zzzzz"
findnextlexicographicstring(s)

s = "z"
findnextlexicographicstring(s)

s = ""
findnextlexicographicstring(s)
