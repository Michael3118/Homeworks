#task1
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_sequence(input_sequence):
    stack = Stack()

    # Push each character onto the stack
    for char in input_sequence:
        stack.push(char)

    # Pop characters from the stack to print in reverse order
    while not stack.is_empty():
        print(stack.pop(), end='')

if __name__ == "__main__":
    # Read a sequence of characters from the user
    user_input = input("Enter a sequence of characters: ")

    # Reverse the sequence using the stack and print the result
    print("Reversed sequence:", end=' ')
    reverse_sequence(user_input)

#task2

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced(sequence):
    stack = Stack()
    opening_symbols = "({["  # Opening symbols
    closing_symbols = ")}]"  # Corresponding closing symbols

    for char in sequence:
        if char in opening_symbols:
            stack.push(char)
        elif char in closing_symbols:
            if stack.is_empty() or not is_matching(stack.pop(), char):
                return False

    return stack.is_empty()

def is_matching(opening, closing):
    return opening == '(' and closing == ')' or \
           opening == '{' and closing == '}' or \
           opening == '[' and closing == ']'

if __name__ == "__main__":
    # Read a sequence of characters from the user
    user_input = input("Enter a sequence of parentheses, braces, and curly brackets: ")

    # Check if the sequence is balanced
    if is_balanced(user_input):
        print("The sequence is balanced.")
    else:
        print("The sequence is not balanced.")

#task3

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, element):
        temp_stack = Stack()
        found = False

        while not self.is_empty():
            current_element = self.pop()
            if current_element == element:
                found = True
                break
            temp_stack.push(current_element)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack.")

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def get_from_queue(self, element):
        temp_queue = Queue()
        found = False

        while not self.is_empty():
            current_element = self.dequeue()
            if current_element == element:
                found = True
                break
            temp_queue.enqueue(current_element)

        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the queue.")

if __name__ == "__main__":
    # Example usage for Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    try:
        result = stack.get_from_stack(2)
        print("Found element in stack:", result)
    except ValueError as e:
        print(e)

    # Example usage for Queue
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')

    try:
        result = queue.get_from_queue('b')
        print("Found element in queue:", result)
    except ValueError as e:
        print(e)
