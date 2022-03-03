from collections import Counter

def findsamesetWords(arr):

    hash={}

    for word in arr:

        worddict=Counter(word)
        key=worddict.keys()
        key=sorted(key)
        key=''.join(key)

        if key in hash:
            hash[key].append(word)
        else:
            hash[key]=[]
            hash[key].append(word)

    for x in hash:
        print(' '.join(hash[x]))

input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle']
findsamesetWords(input)




