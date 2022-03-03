def newstring(charset,s):
    old='abcdefghijklmnopqrstuvwxyz'
    mapchars=dict(zip(charset,old))
    ans=''
    for x in s:
        ans+=mapchars[x]
    return ans
charSet = 'qwertyuiopasdfghjklzxcvbnm'
input = 'utta'
print(newstring(charSet,input))