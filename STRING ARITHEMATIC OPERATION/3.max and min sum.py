def findMinMaxSum(s1,s2):
    x1=s1.replace('6','5')
    x2=s2.replace('6','5')

    print('min sum is',int(x1)+int(x2))

    x1=s1.replace('5','6')
    x2=s2.replace('5','6')
    print('max sum is',int(x1)+int(x2))

x1 = '645'
x2 = '666'
findMinMaxSum(x1,x2)

x1 = '5466'
x2 = '4555'
findMinMaxSum(x1,x2)