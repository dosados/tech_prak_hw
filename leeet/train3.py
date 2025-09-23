class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = {}
        res = 0
        k = 0
        for i, char in enumerate(s):
            if char not in symbols:
                k += 1
                res = max(k, res)
                symbols[char] = i
            
            