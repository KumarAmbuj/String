class Solution:
    def findcomb(self, i, path, k, res, n, li):
        if i > n:
            if k == 0:
                res.append(path.copy())
            return

        for cb in range(li + 1, len(path)):
            path[cb] = i
            self.findcomb(i + 1, path, k - 1, res, n, cb)
            path[cb] = 0

        self.findcomb(i + 1, path, k, res, n, li)

    def combine(self, n: int, k: int):

        path = [0 for i in range(k)]

        res = []

        self.findcomb(1, path, k, res, n, -1)

p=Solution()
res=p.combine(4,2)
print(res)
