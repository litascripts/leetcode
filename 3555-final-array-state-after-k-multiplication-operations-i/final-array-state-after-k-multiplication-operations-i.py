class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        while k:
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
            k -= 1
        return nums