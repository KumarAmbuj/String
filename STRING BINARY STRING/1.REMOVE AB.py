def replaceAB(s):
    count=0

    while('ab' in s):
        s=s.replace('ab','bba',1)
        count+=1
    print(count)
s = 'abbaa'
replaceAB(s)

s = 'aab'
replaceAB(s)

s ='ababab'
replaceAB(s)