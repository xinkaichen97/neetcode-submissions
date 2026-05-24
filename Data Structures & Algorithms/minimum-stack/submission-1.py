class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            diff = 0
            self.minimum = val
        else:
            diff = val - self.minimum
            if diff < 0:
                self.minimum = val
        
        self.stack.append(diff)

    def pop(self) -> None:
        if not self.stack:
            return
        
        diff = self.stack.pop()
        if diff < 0:
            self.minimum = self.minimum - diff

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.minimum
        else:
            return self.minimum

    def getMin(self) -> int:
        return self.minimum
