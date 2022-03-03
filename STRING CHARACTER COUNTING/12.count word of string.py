def fun(list,str):
    list1=str.split()
    result=0
    for x in list:
        if x in list1:
            result+=1
    print(result)
list = ["welcome", "to", "geeks", "portal"]
str = "geeksforgeeks is a computer science portal for geeks"
fun(list,str)
