def findbinary(x):


    m=ord(x)


    res=''
    while(m>0):
        res=str(m%2)+res
        m=m//2
    print(res,end=' ')



def convertToBinary(s):


    for x in s:
        findbinary(x)
    print()

convertToBinary('GFG')
convertToBinary('AMBUJ')
