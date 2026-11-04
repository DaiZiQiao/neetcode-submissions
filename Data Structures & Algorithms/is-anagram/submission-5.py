class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lower = s.lower()
        t_lower = t.lower()

        if len(s_lower) != len(t_lower):
            return False

        alphabet_arr = [0] * 26

        for i in range(len(s_lower)):
            alphabet_arr[ord(s_lower[i]) - ord('a')] += 1

            alphabet_arr[ord(t_lower[i]) - ord('a')] -= 1

        for count in alphabet_arr:
            if count != 0:
                return False
        return True