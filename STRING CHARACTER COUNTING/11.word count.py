out=0
In=1
def fun(str):
    state=out
    wc=0
    for i in range(len(str)):
        if str[i]==' ' or str[i]=='\n' or str[i]=='\t':
            state=out
        elif state==out:
            state=In
            wc=wc+1
    print(wc)
string = "One two         three\n four\tfive "
fun(string)
