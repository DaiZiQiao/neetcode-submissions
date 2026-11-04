class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_window = [0] * 26
        for n in s1:
            s1_window[ord(n) - ord('a')] += 1

        s2_window = [0] * 26
        l = 0
        for r, n in enumerate(s2):
            if r - l + 1 > len(s1):
                s2_window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            s2_window[ord(s2[r]) - ord('a')] += 1
            if s1_window == s2_window:
                return True
        return False