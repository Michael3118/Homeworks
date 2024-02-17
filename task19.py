#task1
def with_index(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1

# Example usage:
my_list = ['apple', 'banana', 'cherry']

for index, value in with_index(my_list, start=1):
    print(f"Index {index}: {value}")

#task2
def in_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

# Example usage:
for number in in_range(1, 10, 2):
    print(number)

#task3
class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return max(0, (self.end - self.start + self.step - 1) // self.step)

# Example usage:
my_iterable = MyIterable(1, 10, 2)

# Using for-in loop
for number in my_iterable:
    print(number)

# Using square brackets syntax
print(my_iterable[2])  # Should print 5
