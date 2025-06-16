class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        tot = n * n
        s = sum(sum(row) for row in grid)
        s0 = tot * (tot + 1) // 2
        diff = s - s0
        sq = sum(sum(x * x for x in row) for row in grid)
        sq0 = tot * (tot + 1) * (2 * tot + 1) // 6
        sum_ab = (sq - sq0) // diff
        a = (diff + sum_ab) // 2
        b = a - diff
        return [a, b] 