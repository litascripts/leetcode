class Solution(object):
    def prefixCount(self, words, pref):
        res = 0;
        for word in words:
            if len(word) >= len(pref) and word[:len(pref)] == pref:
                res += 1;
        
        return res
        