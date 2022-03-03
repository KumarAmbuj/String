def removepattern(s,p):

    while(len(s)!=0):
        index=s.find(p)

        if index==-1:
            return False

        s=s[index+len(p):]
    return True

inp ='GEEKSGEEKSR'
pa ='GEEKS'
print(removepattern(inp, pa))