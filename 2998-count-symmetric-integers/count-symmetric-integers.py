class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2:
                continue
        
            mid = len(s) // 2
            first_half_sum = sum(int(ch) for ch in s[:mid])
            second_half_sum = sum(int(ch) for ch in s[mid:])

            if first_half_sum == second_half_sum:
                count += 1
            
        return count