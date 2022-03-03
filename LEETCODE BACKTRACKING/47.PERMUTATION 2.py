class Solution:
    def findpermute(self, cb, path, hash, n, res):
        if cb == n:
            x = path.copy()
            res.append(x)
            return

        for x in hash:
            if hash[x] > 0:
                path[cb] = x
                hash[x] -= 1
                self.findpermute(cb + 1, path, hash, n, res)
                path[cb] = 0
                hash[x] += 1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        hash = {}

        n = len(nums)
        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = 0
            hash[nums[i]] += 1

        path = [0 for i in range(n)]

        res = []

        self.findpermute(0, path, hash, n, res)

        return res