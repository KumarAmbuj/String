def isPanagram(s):
    a='abcdefghijklmnopqrstuvwxyz'
    s=s.lower()

    for x in a:
        if x not in s:
            return False
    return True

s='The quick brown fox jumps over the lazy dog'
print(isPanagram(s))

s='geeks for geeks'
print(isPanagram(s))