def findmaxdistinct(s):
    prev=''
    ans=-99
    flag=False

    for x in s:

        if x.isupper() and flag==False:
            flag=True
            prev=''
        elif x.isupper() and flag==True:
            ans=max(ans,len(set(prev)))
            prev=''
            flag=True
        
        if x.islower():
            prev=prev+x
    print(ans)



s='zACaAbbaazzC'
findmaxdistinct(s)

s='edxedxxxCQiIVmYEUtLi'
findmaxdistinct(s)