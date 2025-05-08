class Solution:
    def maximumLength(self, s):
        from collections import defaultdict

        count = defaultdict(int)
        n = len(s)

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            # for length L, generate all substrings of length 1 to L
            for l in range(1, length + 1):
                count[s[i] * l] += (length - l + 1)
            i = j

        result = -1
        for key in count:
            if count[key] >= 3:
                result = max(result, len(key))
        return result


