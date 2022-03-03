class Solution:
    def findpermute(self, i, res, S, n, asf):
        if i == n:
            res.append(asf)

        if S[i].isdigit():
            self.findpermute(i + 1, res, S, n, asf + S[i])
        elif S[i].isalpha():
            self.findpermute(i + 1, res, S, n, asf + S[i].upper())
            self.findpermute(i + 1, res, S, n, asf + S[i].lower())

    def letterCasePermutation(self, S: str):

        res = []
        n = len(S)

        self.findpermute(0, res, S, n, '')
        return res
p=Solution()
s='a1b2'
res=p.letterCasePermutation(s)