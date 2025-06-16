# Python version of minOperations
class Solution(object):
    def minOperations(self, nums, k):
        if any(num < k for num in nums):
            return -1
        return len(set(num for num in nums if num > k))