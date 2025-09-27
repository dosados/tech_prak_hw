class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 1
        add_idx = 0
        res_start = 0
        res_end = 0
        for i in range(0, len(s)):

            add_idx = 0
            if i + 1 < len(s) and s[i] == s[i+1]:
                add_idx = 1

            for index in range(0, add_idx + 1):
                j = 1
                k = 1 + index
                while i - j >= 0 and i + j + index < len(s):
                    if s[i-j] == s[i+j + index]:
                        k += 2
                    else:
                        break
                    j += 1
                j -= 1
                

                if k > res:
                    res = k
                    res_start = i - j
                    res_end = i + j + index
            i = res_end

            
        return s[res_start:res_end+1]


s = Solution()

print(s.longestPalindrome("ccc"))