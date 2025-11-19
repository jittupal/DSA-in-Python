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
    def middle(self):
        prev = self.head
        curr = self.head
        while curr is not None and curr.next is not None:
            prev = prev.next
            curr = curr.next
            if curr is None and curr.next is None:
                print("if condition")
                break
            curr = curr.next
        
        print(f"Middle of the linked list is ::  {prev.val}")

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
s.middle()