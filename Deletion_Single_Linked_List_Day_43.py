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
        if x == 1:
            prev = self.head
            self.head = self.head.next
            prev.next = None
            del prev
        else:
            prev = None
            curr = self.head
            count = 1
            while count != x:
                prev = curr
                if curr.next == None:
                    return
                curr = curr.next
                count += 1
            prev.next = curr.next
            curr.next = None
            del curr

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
s.deleteion(6)
s.traversal()
