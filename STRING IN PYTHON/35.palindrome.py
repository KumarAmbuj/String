def fun(str):
    n=len(str)
    if n%2==0:
        first=str[:n//2]
        second=str[n//2:]
    else:
        first=str[:n//2]
        second=str[(n//2+1):]

    for i in range(len(first)):
        if first[i]!=second[len(second)-1-i]:
            print('not a palindrome')
            break
    else:
        print('Palindrome')
fun('malayalam')








