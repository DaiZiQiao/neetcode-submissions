class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0
        

    def push(self, value: int) -> None:
        if self.stack:
            diff = value - self.min
            self.stack.append(diff)
            if diff < 0:
                self.min = value
        else:
            self.stack.append(0)
            self.min = value

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min = self.min - diff
        

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min
        return self.min + diff
        

    def getMin(self) -> int:
        return self.min
        