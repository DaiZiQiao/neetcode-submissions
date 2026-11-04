class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lower = s.lower()
        t_lower = t.lower()

        if len(s_lower) != len(t_lower):
            return False

        alphabet_arr = [0] * 26

        for i in range(len(s_lower)):
            j = ord(s_lower[i]) - ord('a')
            alphabet_arr[j] += 1

            k = ord(t_lower[i]) - ord('a')
            alphabet_arr[k] -= 1

        for i in range(26):
            if alphabet_arr[i] != 0:
                return False
        return True