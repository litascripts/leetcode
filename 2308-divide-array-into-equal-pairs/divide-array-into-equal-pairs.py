class Solution(object):
    def divideArray(self, nums):
        nums.sort()
        return all(nums[i] == nums[i+1] for i in range(0, len(nums), 2))
        