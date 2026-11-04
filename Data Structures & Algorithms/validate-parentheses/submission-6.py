class Solution:
    def isValid(self, s: str) -> bool:
        pair = { ')':'(', '}':'{', ']':'['}
        stk = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)

            else:
                if not stk or stk[-1] != pair[c]:
                    return False
                stk.pop()
        return len(stk) == 0
            