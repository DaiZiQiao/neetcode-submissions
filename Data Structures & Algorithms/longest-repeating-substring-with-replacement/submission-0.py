class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        hashmap = {}
        max_freq = 0

        for right in range(len(s)):
            char = s[right]
            hashmap[char] = hashmap.get(char,0) + 1

            max_freq = max(max_freq, hashmap[char])

            if (right - left + 1) - max_freq > k:
                hashmap[s[left]] -= 1
                left += 1
        
        max_length = max(max_length, right - left + 1)

        return max_length
            


