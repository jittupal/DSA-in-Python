from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.appendleft(x)
        
    def pop(self):
        if len(self.q) == 0:
            return
        self.q.popleft()
        
    def top(self):
        if len(self.q) == 0:
            return -1
        return self.q[0]
        
    def size(self):
        return len(self.q)
        

q = myStack()

q.push(2)
q.push(3)
q.push(5)
q.push(4)
q.pop()
print(q.top())
print(q.size())