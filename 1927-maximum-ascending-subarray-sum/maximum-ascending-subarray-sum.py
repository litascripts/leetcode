class Solution(object):
    def maxAscendingSum(self, nums):
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
            ans = max(ans, curr)
        return ans
        