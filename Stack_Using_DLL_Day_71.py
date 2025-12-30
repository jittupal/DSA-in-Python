class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        
    def top(self):
        if self.tail == None:
            print("Stack Is Empty")
        else:
            print(self.tail.val)
    
    def pop(self):
        if self.tail == None:
            print("Stack Is Empty Pop")
        else:
            print("Pop Called", self.tail.val)
            if self.tail.prev == None:
                print("Only One element")
                self.head = self.tail = None
            else: 
                self.tail = self.tail.prev
                self.tail.next = None
                
    def isEmpty(self):
        if self.tail == None:
            print("Stack is Empty")
        else:
            print("Stack Has Elements")
            
s = DLL()
s.push(7)
s.push(8)
s.push(3)
s.top()
s.push(5)
s.push(2)
s.pop()
s.top()
s.pop()
s.pop()
s.pop()
s.pop()
s.isEmpty()