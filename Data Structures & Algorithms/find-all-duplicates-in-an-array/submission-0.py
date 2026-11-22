class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                res.append(abs(nums[i]))
        return res