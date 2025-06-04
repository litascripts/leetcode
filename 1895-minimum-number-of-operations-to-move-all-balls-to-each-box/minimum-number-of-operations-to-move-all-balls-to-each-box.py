class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        ans = [0] * n
        count = x = 0
        for i in range(n):
            ans[i] = x
            count += boxes[i] == '1'
            x += count
        
        x = count = 0
        for i in range(n - 1, -1, -1):
            ans[i] += x
            count += boxes[i] == '1'
            x += count

        return ans