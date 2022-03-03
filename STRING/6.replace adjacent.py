def fun(st):
    i=0
    while i< len(st)-1:
        if st[i]==st[i+1]:
            st.replace(st[i],'')
        else:
            i=i+1
    print(st)
    