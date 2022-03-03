def findcamelcase(arr,s):
    flag=False
    for i in range(len(arr)):

        x=arr[i]

        for j in s:
            if j not in x:
                break
        else:
            flag=True
            print(x)
    if flag==False:
        print('not found')
    print()
dict = ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab","GeeHks"]

s= "HT"
findcamelcase(dict,s)

s='H'
findcamelcase(dict,s)

s='HTC'
findcamelcase(dict,s)

s='KBC'
findcamelcase(dict,s)
