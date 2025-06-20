class Solution(object):
    def maxDistance(self, s, k):
        n = len(s)
        N = S = E = W = ans = 0
        for i in range(n):
            if s[i] == 'N':
                N += 1
            if s[i] == 'S':
                S += 1
            if s[i] == 'E':
                E += 1
            if s[i] == 'W':
                W += 1
            dist = abs(N - S) + abs(E - W) + 2 * k
            ans = max(ans, min(dist, i + 1))
        return ans