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
    def lengthOfCycle(self):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
              slow = slow.next
              fast = fast.next.next
              if slow == fast:
                 slow = slow.next
                 count = 1
                 while slow != fast:
                       slow = slow.next
                       count += 1
                print("Length of Cycle in Linked List is: ", count)
          print("There is no Cycle)

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
s.lengthOfCycle()
