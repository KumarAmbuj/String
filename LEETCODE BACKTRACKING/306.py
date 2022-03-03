class Solution:
    def findnumber(self, s, l1, l2, nums, n):

        num1 = int(nums[s:l1])
        num2 = int(nums[s + l1:s + l1 + l2])
        num3 = str(num1 + num2)

        print(num1,num2)

        l3 = len(num3)

        if l3 > (n - l1 - l2 - s):
            return False

        if num3 == nums[s + l1 + l2:s + l1 + l2 + l3]:

            if s + l1 + l2 + l3 == n:
                return True

            return self.findnumber(s + l1, l2, l3, nums, n)

    def isAdditiveNumber(self, nums: str) -> bool:

        n = len(nums)

        for i in range(1, n):
            for j in range(1, n):

                if i + j < n:

                    if self.findnumber(0, i, j, nums, n):
                        return True
        return False
nums="112358"
p=Solution()
res=p.isAdditiveNumber(nums)
