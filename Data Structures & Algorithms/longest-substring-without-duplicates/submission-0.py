class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        hashset = set()
        longest_substring = 0

        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                longest_substring = max(longest_substring, right - left + 1)
                right += 1
            else:
                hashset.remove(s[left])
                left += 1
        return longest_substring