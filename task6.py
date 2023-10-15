#task1
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]

largest = random_numbers[0]


index = 1
while index < len(random_numbers):
    if random_numbers[index] > largest:
        largest = random_numbers[index]
    index += 1

print("List of random numbers:", random_numbers)
print("The largest number is:", largest)


#task2

import random

list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [random.randint(1, 10) for _ in range(10)]

common_list = []

index = 0
while index < len(list1):
    num = list1[index]
    if num in list2 and num not in common_list:
        common_list.append(num)
    index += 1

print("List 1:", list1)
print("List 2:", list2)
print("\nCommon List without duplicates:", common_list)


#task3

result_list = []

num = 1

while num <= 100:
    if num % 7 == 0 and num % 5 != 0:
        result_list.append(num)
    num += 1

print("\nNumbers divisible by 7 but not multiple of 5:", result_list)













