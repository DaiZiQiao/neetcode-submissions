class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if stack and c == hashmap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack