def fun(str,k):
    print(str)
    temp=''
    freq=0
    st=''
    i=0
    while(i<len(str)):
        temp=''
        freq=0
        while(i<len(str) and str[i]>='a' and str[i]<='z'):
            temp=temp+str[i]
            i=i+1
        while(i<len(str) and str[i]>='1' and str[i]<='9'):
            n=int(str[i])
            freq=freq*10+n
            i=i+1

        for j in range(freq):
            st=st+temp
    print(st[k-1])

st="ab4c12ed3"
fun(st,21)
