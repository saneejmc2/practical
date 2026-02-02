#Create a linked list with insert and traverse methods.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    
class SinglyLinkedList:
    def __init__(self):
        self.head = None    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   
def main():
    sll = SinglyLinkedList()
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    sll.traverse()  # Output: 10 -> 20 -> 30 -> None
if __name__ == "__main__":
    main()  
    