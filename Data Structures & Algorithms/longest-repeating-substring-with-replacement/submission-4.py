class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        substr = 0
        d = {}

        max_fr = 0
        for i,n in enumerate(s):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

            max_fr = max(max_fr, d[s[i]])
            while (i - l + 1) - max_fr > k:
                
                d[s[l]] -= 1
                l += 1
            substr = max(substr, i - l + 1)

        return substr