#task1

def binary_search_recursive(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, mid + 1, high, target)
        else:
            return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return -1

# Приклад використання:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Елемент {target} знаходиться на позиції {result}.")
else:
    print(f"Елемент {target} не знайдено.")

#task2

def fibonacci_search(arr, target):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i

        elif arr[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1

    return -1

# Приклад використання:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = fibonacci_search(arr, target)

if result != -1:
    print(f"Елемент {target} знаходиться на позиції {result}.")
else:
    print(f"Елемент {target} не знайдено.")

#task3

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def __contains__(self, key):
        index = self._hash(key)
        return self.table[index] is not None and key in dict(self.table[index])

    def __len__(self):
        count = 0
        for item in self.table:
            if item is not None:
                count += len(item)
        return count

# Приклад використання:
my_hash_table = HashTable()

my_hash_table.table[3] = {'apple': 5, 'banana': 7}
my_hash_table.table[8] = {'orange': 3, 'grape': 9}

print('apple' in my_hash_table)  # True
print('banana' in my_hash_table)  # True
print('orange' in my_hash_table)  # True
print('grape' in my_hash_table)  # True
print('kiwi' in my_hash_table)  # False

print(len(my_hash_table))  # 4 (total number of key-value pairs)
