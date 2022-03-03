class WordDictionary:

    def __init__(self):
        self.hash = set()

    def addWord(self, word: str) -> None:

        self.hash.add(word)

    def findword(self, i, word, asf):

        if i == len(word):
            print(asf)
            if asf in self.hash:

                return True
            return False

        if word[i] != '.':
            return self.findword(i + 1, word, asf + word[i])
        elif word[i] == '.':
            for k in range(0, 26):
                x = asf + chr(k+ord('a'))
                if self.findword(i + 1, word, x):
                    return True
        return False

    def search(self, word: str) -> bool:

        return self.findword(0, word, '')

p=WordDictionary()
p.addWord('bad')
p.addWord('dad')
p.addWord('mad')

print(p.search('b..'))



