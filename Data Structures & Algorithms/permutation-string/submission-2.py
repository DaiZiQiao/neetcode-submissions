class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}

        for c in s1:
            s1_dict[c] = s1_dict.get(c,0) + 1
        
        window = len(s1)
        left = 0

        for right in range(len(s2)):
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1
            if right - left + 1 > window:
                s2_dict[s2[left]] -= 1

                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1

            if s1_dict == s2_dict:
                return True
        return False
        