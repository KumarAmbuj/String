def fun(str):
    nospace=[ch for ch in str if ch!=' ']
    space=len(str)-len(nospace)
    result=' '*space

    print(result+''.join(nospace))
input = 'move these spaces to beginning'
fun(input)