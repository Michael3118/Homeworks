#task1
import random

random_number = random.randint(1, 10)

user_guess = int(input("Guess the number between 1 and 10: "))

if user_guess == random_number:
    print("Congratulations! You guessed the correct number:", random_number)
else:
    print("Sorry, the correct number was:", random_number)


#task2

name_guess = input()
age_guess = int(input())
print(f'Hello {name_guess}, on your next birthday you’ll be {age_guess+1} years'   )


#task3

input_string = input("Enter a string: ")

for _ in range(5):
    random_str = ''.join(random.sample(input_string, len(input_string)))
    print(random_str)