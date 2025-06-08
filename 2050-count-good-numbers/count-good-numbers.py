class Solution(object):
    def countGoodNumbers(self, n):
        mod = 10 ** 9 + 7
        odd = n // 2
        even = (n + 1) // 2

        return (pow(5, even, mod) * pow(4, odd, mod)) % mod
        