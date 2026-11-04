class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        counter = 0
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            counter = max(counter, right - left + 1)
        return counter