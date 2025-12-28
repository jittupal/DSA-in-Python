class myQueue:
    def __init__(self, n):
        self.queue = []
        self.n = n

    
    def isEmpty(self):
        return len(self.queue) == 0

    
    def isFull(self):
        return len(self.queue) == self.n

    
    def enqueue(self, x):
        if len(self.queue) == self.n:
            return -1
        self.queue.append(x)

    
    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    
    def getFront(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
       
    
    def getRear(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
        

queue = myQueue(5)
print(queue.enqueue(5))
print(queue.enqueue(7))
print(queue.enqueue(8))
print(queue.enqueue(6))
print(queue.getFront())
print(queue.getRear())
print(queue.dequeue())
print(queue.isEmpty())
print(queue.isFull())
