def EncodingString(string):
    odd=[0]*26
    even=[0]*26


    for i in range(len(string)):
        if i%2==0:
            even[ord(string[i])-ord('a')]+=1
        else:
            odd[ord(string[i]) - ord('a')] += 1

    encoding=''
    for i in range(26):
        encoding=encoding+str(even[i])
        encoding+='-'
        encoding+=str(odd[i])
        encoding+='-'

    return encoding



def findDistinctString(arr):
    s=set()
    count=0

    for i in range(len(arr)):

        x=EncodingString(arr[i])
        if x not in s:
            s.add(x)
            count+=1

    return count
input = ["abcd", "acbd", "adcb",
             "cdba", "bcda", "badc"]
print(findDistinctString(input))

arr = ["abcd", "cbad", "bacd"]
print(findDistinctString(arr))





