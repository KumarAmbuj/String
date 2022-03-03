class Solution:
    def findnumber(self, nums, beg, len1, len2, n):

        s1 = nums[beg:(beg + len1)]
        s2 = nums[beg + len1:beg + len1 + len2]

        if len(s1) > 1 and s1[0] == '0':
            return False
        if len(s2) > 1 and s2[0] == '0':
            return False

        s3 = str(int(s1) + int(s2))
        len3 = len(s3)

        print(s1,s2)

        if len3<max(len1,len2):
            return False

        if len3 > (n - len1 - len2 - beg):
            return False
        x1=s3
        x2=nums[beg + len1 + len2:beg + len1 + len2 + len3]

        print(x1,x2,x1==x2)

        if x1==x2:


            if beg + len1 + len2 + len3 == n:
                return True

            return self.findnumber(nums, beg + len1, len2, len3, n)
        return False

    def isAdditiveNumber(self, nums: str) -> bool:

        n = len(nums)

        for i in range(1, n):
            for j in range(1, n):
                if i + j < n:

                    if self.findnumber(nums, 0, i, j, n):
                        return True
        return False


p=Solution()
res=p.isAdditiveNumber("199001200")
print(res)