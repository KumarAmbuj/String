class Solution:
    def findmax(self, i, res, n, asf, arr):
        if i == n:
            res[0] = max(res[0], len(asf))
            return

        x = arr[i]

        xl = len(x)
        c = 0

        for z in x:
            if z not in asf:
                c += 1
        if c == xl:
            self.findmax(i + 1, res, n, asf + x, arr)
        self.findmax(i + 1, res, n, asf, arr)

    def maxLength(self, arr):

        res = [0]

        n = len(arr)

        self.findmax(0, res, n, '', arr)
        return res[0]


arr=["yy","bkhwmpbiisbldzknpm"]
p=Solution()
res=p.maxLength(arr)
print(res)