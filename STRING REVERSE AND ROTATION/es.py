l=[1,2,3,4]
l1=[4,1,2,3]
l=l[len(l)-1:]+l[:len(l)-1]
print(l==l1)