class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        val = 0
        for t in tokens:
            if t not in ops:
                stack.append(t)
            else:
                n1, n2 = int(stack.pop()), int(stack.pop())
                val = n1 + n2 if t == '+' else n2 - n1 if t == '-' else n1*n2 if t == '*' else n2/n1
                stack.append(val)
        return val if len(stack) == 0 else int(stack[-1])