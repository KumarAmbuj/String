class Solution:
    def findpermute(self, i, path, res, K, k, n):
        if i > n:
            K[0] += 1
            res.append(''.join(path))
            return


        for box in range(n):
            if path[box] == '':
                path[box] = str(i)
                self.findpermute(i + 1, path, res, K, k, n)
                path[box] = ''

    def getPermutation(self, n: int, k: int):

        path = ['' for i in range(n)]
        res = []
        K = [0]

        self.findpermute(1, path, res, K, k, n)
        print(res)
        print(K[0])


p=Solution()
res=p.getPermutation(4,9)
res=p.getPermutation(3,9)