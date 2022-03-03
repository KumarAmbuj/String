def findfirstoccurence(arr):
    inDLL=[]
    repeated=[False]*256

    for i in range(len(arr)):
        x=arr[i]

        print('reading',x)

        if not repeated[ord(x)]:

            if x not in inDLL:
                inDLL.append(x)

            else:
                inDLL.remove(x)
                repeated[ord(x)]=True
        if len(inDLL)!=0:
            print('first occurence is',inDLL[0])

s= "geekforgeekandgeeksandquizfor"
findfirstoccurence(s)
