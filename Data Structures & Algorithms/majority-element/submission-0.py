class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        vote = count = 0
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
            if freq[i] > count:
                vote = i
                count = freq[i]

        return vote