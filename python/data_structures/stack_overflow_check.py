#Stack Class with Overflow Check
#Implement a Stack class with push, pop, peek methods that handles overflow (max 5 elements) and underflow conditions.
import json

class Stack:
    def __init__(self, max_size=5):
        # Initialize stack
        self.max_size = max_size
        self.items = []

    def push(self, item):
        # Add item, return "Overflow" if full
        if len(self.items) >= self.max_size:
            return "Overflow"
        self.items.append(item)
#        print(self.items)
        return #"Item pushed successfully"

    def pop(self):
        # Remove and return item, return "Underflow" if empty
        if not self.items:
            return "Underflow"
        return self.items.pop()

    def peek(self):
        # Return top item without removing
        if not self.items:
            return "Underflow"
        return self.items[-1]

# Test your implementation
#s = Stack()
#push1 = s.push(10)
#push2 = s.push(20)
#peek = s.peek()
#pop = s.pop()
#output = {
#    "push1": push1,
#    "push2": push2,
#    "peek": peek,
#    "pop": pop,
##    "stack": s.__dict__
#}
#print(json.dumps(output))  

# Test your implementation
s = Stack()
print(s.push(10))
print(s.push(20))
print(s.peek())
print(s.pop())