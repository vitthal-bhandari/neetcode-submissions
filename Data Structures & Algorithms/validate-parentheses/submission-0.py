class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(', '{', '[']
        close = [')', '}', ']']
        stack = []
        for c in s:
            if c in op:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if not ((c == ')' and last == '(') or (c == '}' and last == '{') or (c == ']' and last == '[')):
                    return False
                stack.pop()
        return True if len(stack) == 0 else False
