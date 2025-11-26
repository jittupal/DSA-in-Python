class Node:
    def __init__(self, var):
        self.var = var
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    
    def insertAtHead(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def traverDLL(self):
        curr = self.head
        while curr is not None:
            print(curr.var, end=" ")
            curr = curr.next  
    def insertAtEnd(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            
            curr.next = new_node
            new_node.prev = curr
    def insertInBetween(self, value, pos):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            count = 1
            while curr is not None and count < pos-1:
                curr = curr.next
                count += 1
            
            if curr is None:
                print("Position Is Out Of Index")
            
            new_node.prev = curr
            new_node.next = curr.next
            curr.next.prev = new_node
            curr.next = new_node
            
    def findpair(self, target):
        back = self.head
        while back.next is not None:
            back = back.next
            print("Back Positon :: ", back.var)
            
        curr = self.head
        ans = []
        
        while curr.prev != back:
            sum = curr.var + back.var
            if sum == target:
                temp = [curr.var, back.var]
                ans.append(temp)
                curr = curr.next
                print("Curr Position :: ", curr.var)
                back = back.prev
            elif sum > target:
                back = back.prev
            else:
                curr = curr.next
                print("Curr Position :: ", curr.var)
        
        print(ans)
            

D = DLL()

# D.insertAtHead(1)
# D.insertAtHead(2)
# D.insertAtHead(3)
# D.insertAtHead(4)
# D.insertAtHead(5)
# D.insertAtHead(6)
D.traverDLL()
print()
D.insertAtEnd(1)
D.insertAtEnd(2)
D.insertAtEnd(3)
D.insertAtEnd(4)
D.insertAtEnd(5)
D.insertAtEnd(6)
D.insertAtEnd(8)
D.insertAtEnd(9)
D.traverDLL()
print()
# D.insertInBetween(4, 4)
# D.insertInBetween(3, 2)
# D.insertInBetween(1, 7)
D.traverDLL()
D.findpair(7)

