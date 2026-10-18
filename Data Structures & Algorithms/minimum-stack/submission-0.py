class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.min.append(min(value, self.min[-1])) if len(self.min) > 0 else self.min.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) > 0 else -1

    def getMin(self) -> int:
        return self.min[-1] if len(self.min) > 0 else -1
        
