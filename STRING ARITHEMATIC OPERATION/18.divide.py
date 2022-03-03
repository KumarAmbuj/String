def divide(s1,s2):
    if len(s2)>len(s1):
        s1,s2=s2,s1

    quo=''
    rem=''

    i=0
    a=''
    while(i<len(s1)):

        a=a+s1[i]

        quo=quo+str(int(a)//int(s2))
        rem=str(int(a)%int(s2))
        a=rem
        i+=1



    print('quotient is',quo.lstrip('0'))
    print('remainder is',rem)
divide('12','4')

number  = '1260257'
divisor = '37'

divide(number,divisor)

number  = '12313413534672234'
divisor = '754'
divide(number,divisor)

number = "1248163264128256512";
divisor = '125'
divide(number,divisor)

number = "12345678";
divisor = '7'
divide(number,divisor)