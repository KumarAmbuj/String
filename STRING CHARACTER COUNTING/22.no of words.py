from collections import Counter
def fun(input):
    dict={}

    for word in input:
        worddict=Counter(word)
        key=worddict.keys()
        key=sorted(key)

        key=''.join(key)

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key]=[]
            dict[key].append(word)
    print(dict)
    for (key,value) in dict.items():
        print(','.join(dict[key]))
input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle']
fun(input)