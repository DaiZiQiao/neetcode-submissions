class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min:
            self.min.append(min(self.min[-1], value))
        else:
            self.min.append(value)
    
    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.min[-1]