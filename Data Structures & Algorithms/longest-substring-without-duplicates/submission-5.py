class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_s = set()
        l = 0
        length = 0

        for c in s:
            while c in cur_s:
                cur_s.remove(s[l])
                l += 1
            cur_s.add(c)
            length = max(length, len(cur_s))
        
        return length