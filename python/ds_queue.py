queue = []

def enqueue(item):
    queue.append(item)
    print(item, "enqueued")

def dequeue():
    if not queue:
        return None
    print(queue[0], "dequeued")
    return queue.pop(0)

def peek():
    if not queue:
        return None
    print(queue[0], "peeked")
    return queue[0]

def is_empty():
    return len(queue) == 0

def main():
    enqueue(1)
    enqueue(2)
    enqueue(3)
    
    print("queue: ",queue)
    print(dequeue())
    print("queue: ",queue)
    print(peek())
    print(is_empty())
    print(dequeue())
    print(dequeue())
    print(is_empty())

if __name__ == "__main__":
    main()
