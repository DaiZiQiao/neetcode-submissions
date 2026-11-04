class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        substr = 0
        d = {}

        for i,n in enumerate(s):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

            max_fr = max(d.values())
            while (i - l + 1) - max_fr > k:
                
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            substr = max(substr, i - l + 1)
               
        if substr == 0:
            return len(s)
        return substr