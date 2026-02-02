stack = []

def push(item):
    stack.append(item)
    print(item, "pushed")

def pop():
    if len(stack) == 0:
        print("stack is empty")
        return None
    print(stack[-1], "popped")
    return stack.pop()

def peek():
    if len(stack) == 0:
        print("stack is empty")
        return None
    print(stack[-1], "peeked")
    return stack[-1]

def is_empty():
    return len(stack) == 0

def main():
    push(1)
    push(2)
    push(3)
    print("stack: ",stack)
    print("pop: ",pop())
    print("stack: ",stack)
    print("peek: ",peek())
    print("is_empty: ",is_empty())
    print("pop: ",pop())
    print("pop: ",pop())
    print("is_empty: ",is_empty())

if __name__ == "__main__":
    main()