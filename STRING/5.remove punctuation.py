def fun(st):
    p='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    for x in st:
        if x in p:
            st=st.replace(x,'')
    print(st)
string = "Welcome???@@##$ to#$% Geeks%$^for$%^&Geeks"
fun(string)