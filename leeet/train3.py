
def lengthOfLongestSubstring(s: str) -> int:
    symbols = {}
    res = 0
    start_idx = 0
    k = 0
    for i, char in enumerate(s):
        if char in symbols:
            start_idx = max(symbols[char], start_idx)
        k = i - start_idx + 1
        res = max(k, res)
        symbols[char] = i + 1
    return res
            

print(lengthOfLongestSubstring("ammzuhta"))
print(lengthOfLongestSubstring("abc"))
print(lengthOfLongestSubstring("abba"))


