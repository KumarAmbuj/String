from collections import Counter

def findsequenceofanagram(arr):
    hash={}


    for x in arr:
        word=Counter(x)
        key=word.keys()
        key=sorted(key)
        key=''.join(key)
        if key in hash:
            hash[key].append(x)
        else:
            hash[key]=[]
            hash[key].append(x)

    for x in hash:
        print(','.join(hash[x]))

arr=["cat", "dog", "tac", "god", "act", "gdo"]
findsequenceofanagram(arr)
