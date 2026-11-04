class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        result = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in dict:
                dict[s[right]] = 1
            else:
                dict[s[right]] += 1
            
            
            while (right - left + 1) - max(dict.values()) > k:
                dict[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result