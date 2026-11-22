class Solution(object):
    def findDisappearedNumbers(self, nums):
        numbers = set(nums)
        res = []

        for n in range(1,len(nums)+1):
            if n not in numbers:
                res.append(n)

        return res
