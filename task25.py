#task1

class UnsortedList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            raise ValueError(f"{item} not found in the list.")

    def pop(self, index=None):
        if self.is_empty():
            raise IndexError("pop from an empty list")

        if index is None:
            return self.items.pop()
        else:
            try:
                return self.items.pop(index)
            except IndexError:
                raise IndexError("pop index out of range")

    def insert(self, index, item):
        if index < 0 or index > len(self.items):
            raise IndexError("list index out of range")

        self.items.insert(index, item)

    def slice(self, start, stop):
        if start < 0 or start >= len(self.items) or stop < 0 or stop > len(self.items) or start >= stop:
            raise ValueError("Invalid start or stop values for slicing")

        return self.items[start:stop]

if __name__ == "__main__":
    # Example usage for UnsortedList
    my_list = UnsortedList()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    print("Original List:", my_list.items)

    # Index
    try:
        index = my_list.index(3)
        print("Index of 3:", index)
    except ValueError as e:
        print(e)

    # Pop
    popped_item = my_list.pop(1)
    print("Popped item at index 1:", popped_item)
    print("List after pop:", my_list.items)

    # Insert
    my_list.insert(1, 5)
    print("List after insert 5 at index 1:", my_list.items)

    # Slice
    sliced_list = my_list.slice(1, 3)
    print("Sliced list from index 1 to 3:", sliced_list)

#task2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")

        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")

        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    # Example usage for LinkedListStack
    stack = LinkedListStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Top of the stack:", stack.peek())

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    print("Stack size after pop:", stack.size())

#task3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")

        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_item

    def front_element(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")

        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    # Example usage for LinkedListQueue
    queue = LinkedListQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue size:", queue.size())
    print("Front of the queue:", queue.front_element())

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)

    print("Queue size after dequeue:", queue.size())
