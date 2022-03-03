class Solution:
    def findpermute(self, path, res, K, k, n, asf):
        if len(asf) == n:
            K[0] += 1
            if K[0] == k:
                res[0] = asf
                print(asf)
            return
        if K[0] > k:
            return

        for i in range(n):
            if i not in path:
                s = asf + str(i + 1)
                path.append(i)
                self.findpermute(path, res, K, k, n, s)
                path.pop()

    def getPermutation(self, n: int, k: int) -> str:

        path = []
        res = ['']
        K = [0]
        asf = ''

        self.findpermute(path, res, K, k, n, asf)
        return res[0]
p=Solution()
res=p.getPermutation(9,353955)
