class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            
            curr.next = new_node
    def traversal(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end="  ")
            curr = curr.next
    def deleteion(self, x):
        fast = self.head
        slow = self.head
        
        for _ in range(x):
            fast = fast.next
            
        if fast is None:
            self.head = self.head.next
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        

s = SLL()
s.append(5)
s.append(8)
s.append(7)
s.append(5)
s.append(9)
s.append(2)
s.append(6)
s.traversal()
print()
s.deleteion(3)
s.traversal()
print()
s.deleteion(5)
s.traversal()
