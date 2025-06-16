class Solution(object):
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num # step 1: compute bitwise OR of all numbers
        return total * (1 << (len(nums) - 1)) # step 2: multiply by 2^(n-1)