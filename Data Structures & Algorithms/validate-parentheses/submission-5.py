class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')':'(', '}':'{', ']':'['}
        stk = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stk.append(s[i])

            else:
                if not stk or stk[-1] != pair[s[i]]:
                    return False
                stk.pop()
        return len(stk) == 0
            