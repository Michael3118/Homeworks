#task1
def count_local_variables():
    a = 10
    b = "Hello"
    c = [1, 2, 3]
    d = {'key': 'value'}

    local_vars = locals()
    return len(local_vars)

# Function call
num_local_vars = count_local_variables()
print("Number of local variables in the function:", num_local_vars)

#task2

def calculator(*args, operator = '+'  ):
    operator_of_func = choose_operation(operator)
    print(operator_of_func(args))
    a = 2
    print(f"Function {calculator.__name__} completed with args: {args} and {operator_of_func.__name__}")

def choose_operation( operator: str ):
    if operator == '+':
        return sum
    elif operator == '/':
        return division
def division(args):
    start = 1
    for value in args:
        start *= value
        return start

calculator(5, 10 , 12, 15, 38, operator = '/' )

print(calculator)
print(type(calculator))
print(calculator.__name__)

print(calculator.__code__.co_varnames)

#task3
def choose_func(nums, func1, func2):
    # Check if all numbers in the list are positive
    if all(num > 0 for num in nums):
        return func1(nums)  # Execute the first function on the list
    else:
        return func2(nums)  # Execute the second function on the list

# Given functions
def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

