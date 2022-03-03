def fun(str):
    upper=0
    lower=0
    number=0
    special=0

    for i in range(len(str)):
        if str[i]>='A' and str[i]<='Z':
            upper+=1
        elif str[i]>='a' and str[i]<='z':
            lower+=1
        elif str[i]>='0' and str[i]<='9':
            number+=1
        else:
            special+=1
    print('upper ',upper)
    print('lower ',lower)
    print('number ',number)
    print('special ',special)
str = "#GeeKs01fOr@gEEks07"
fun(str)