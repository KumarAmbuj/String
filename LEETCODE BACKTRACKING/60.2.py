class Solution:
    def findpermute(self, i, l, res, K, k, n):
        if K[0] > k:
            return
        if i == n:
            K[0] += 1
            print(''.join(l))
            if K[0] == k:
                res[0] = ''.join(l)
            return

        for c in range(i, n):
            l[c], l[i] = l[i], l[c]
            self.findpermute(i + 1, l, res, K, k, n)
            l[c], l[i] = l[i], l[c]

    def getPermutation(self, n: int, k: int) -> str:

        res = ['']
        K = [0]
        asf = ''
        l = [str(i + 1) for i in range(n)]
        self.findpermute(0, l, res, K, k, n)
        return res[0]

p=Solution()
n=3
k=5
res=p.getPermutation( n, k)
print(res)