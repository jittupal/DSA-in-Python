class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            mini = min(self.stack[-1][1], val)
            self.stack.append([val, mini])
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        print(self.stack[-1][0])

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return
        print(self.stack[-1][1])
    
s = MinStack()
s.push(3)
s.push(4)
s.push(8)
s.push(9)
s.getMin()
s.top()
s.pop()
s.pop()
s.getMin()

