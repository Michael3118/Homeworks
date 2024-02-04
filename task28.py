#task1

def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        # Pass from left to right (upwards)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break  # If no swap occurred, the list is already sorted

        swapped = False

        # Pass from right to left (downwards)
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

    return arr

#task2

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # If there are any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print("Sorted List:", my_list)

#task3

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        arr = quicksort(left) + middle + quicksort(right)
    return arr

# Example usage:
import random

my_list = random.sample(range(1, 100), 20)
print("Original List:", my_list)
sorted_list = quicksort(my_list)
print("Sorted List:", sorted_list)
