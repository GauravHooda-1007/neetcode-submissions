class Solution(object):
    def majorityElement(self, nums):
        vote = None
        count  = 0
        for i in nums:
            if count == 0:
                vote = i
            if i == vote:
                count+=1
            else: 
                count -=1
        return vote