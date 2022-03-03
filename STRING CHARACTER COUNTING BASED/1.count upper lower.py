def countchar(s):
    upp=0
    low=0
    number=0
    special=0

    for x in s:
        if x.isupper():
            upp+=1
        elif x.islower():
            low+=1
        elif x.isdigit():
            number+=1
        else:
            special+=1

    print('upper',upp)
    print('lower',low)
    print('number',number)
    print('special',special)
s='#GeeKs01fOr@gEEks07'
countchar(s)

