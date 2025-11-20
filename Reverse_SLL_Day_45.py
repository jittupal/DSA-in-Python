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
    def reverses(self):
        prev = None
        temp = self.head
        while temp is not None:
            forward = temp.next
            temp.next = prev
            prev = temp
            temp = forward
        self.head = prev


s = SLL()
s.append(5)
s.append(8)
s.append(7)
s.append(5)
s.append(9)
s.append(2)
s.append(3)
s.append(6)
s.traversal()
print()
s.reverses()
s.traversal()