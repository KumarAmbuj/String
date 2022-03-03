def fun(s):
    s=s.lower()

    a='abcdefghijklmnopqrstuvwxyz'
    count=0
    for x in a:
        if x not in s:
            count=count+1
    if count==0:
        print('pangram')
    elif count==1:
        print('its a pangramatic lipogram')
    else:
        print('not')


fun('The quick brown fox jum over the lazy dog')
