class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for char in s:
            if char in parenthesis:
                if stack and stack[-1] == parenthesis[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False