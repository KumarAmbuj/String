def change(ch):
    return '1' if ch == '0' else '0'

def makealternative(s):
    arr=list(s)
    count=0

    prev=arr[0]
    n=len(arr)

    for i in range(1,len(arr)):

        if prev!=s[i]:
            prev=s[i]
            continue

        elif prev==s[i]:

            x=change(prev)

            if (i+1)==n or prev!=s[i+1]:

                arr[i-1]=x
                prev=s[i]
                count+=1
            else:
                arr[i]=x
                prev=x
                count+=1

    print(count)
s = '0001010111'
makealternative(s)

s = '001'
makealternative(s)

