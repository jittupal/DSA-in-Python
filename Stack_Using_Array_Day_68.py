class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) == 0:
            print("Empty Stack")
        print(self.stack.pop())
    
    def top(self):
        if len(self.stack) == 0:
            print("Empty Stack")
        print(self.stack[-1])
    
    def size(self):
        print(len(self.stack))
    
s = Stack()
s.push(90)
s.push(78)
s.push(12)
s.size()
s.pop()
s.top()
s.push(34)
s.push(56)
s.top()
s.pop()