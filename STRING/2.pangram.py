def pangram(string):
    a='abcdefghijklmnopqrstuvwxyz'

    for x in a:
        if x not in string:
            print('not a pangram')

            break
    else:
        print('pangram')
pangram("The quick brown fox jumps over the little lazy dog")

