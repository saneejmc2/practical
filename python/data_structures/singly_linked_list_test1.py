#Create a linked list with insert and traverse methods.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def isEmpty(self):
        return self.head is None

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next

ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.traverse()