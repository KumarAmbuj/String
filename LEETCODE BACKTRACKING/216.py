class Solution:
    def findcombine(self, i, path, res, k, sm, n):
        if k < 0 or sm > n:
            return
        if i == 10:
            if k == 0:
                res.append(path.copy())
            return

        path.append(i)
        self.findcombine(i + 1, path, res, k - 1, sm + i, n)
        path.pop()

        self.findcombine(i + 1, path, res, k, sm, n)

    def combinationSum3(self, k: int, n: int) :
        path = []
        res = []
        
        sm = 0

        self.findcombine(1, path, res, k, sm, n)
        return res


