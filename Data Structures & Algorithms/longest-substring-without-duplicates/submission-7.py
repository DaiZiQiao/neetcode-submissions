class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_s = {}
        l = 0
        length = 0

        for r,c in enumerate(s):
            if c in cur_s and cur_s[c] >= l:
                l = cur_s[c] + 1
            cur_s[c] = r
            length = max(length, r - l + 1)
        
        return length