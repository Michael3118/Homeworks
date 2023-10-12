#task1
str1 = 'helloworld'
l = len(str1)
str2 = ""

for i in range(0, len(str1) ):
    if l < 3:
        break
    else:
        if i in (0,1,l-2,l-1):
            str2 = str2 + str1[i]
        else:
            continue
print('str1= ' + str1 )
print('str2= ' + str2)


str3 = 'my'
count = 0
for i in str3:
    count = count + 1
    str4 = str3 [0:2] + str3 [count - 2:count]
print('str3= ' + str3 )
print('str4= ' + str4)


str5 = 'x'
count = 0
for i in str5:
    str6 = str5 [-1:0 ]
print('str5= ' + str5 )
print('str6= ' + str6)

#task2


def valid_phone_number(input_string):
    return input_string.isdigit() and len(input_string) == 10


while True:
    phone_number = input("Enter a 10-digit phone number: ")

    if valid_phone_number(phone_number):
        print("Thanks")
        break
    else:
        print("Invalid phone number. Please enter a 10-digit number with no spaces or special characters.")


#task3

import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operator = random.choice(['+', '-', '*', '/'])

question = f"What is {num1} {operator} {num2}? "
correct_answer = eval(f"{num1} {operator} {num2}")

user_answer = float(input(question))

if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"Wrong. The correct answer is {correct_answer}.")

#task4

self_input1 = "anton"
while True:

    self_input = input("My name is ")

    if self_input.lower() == self_input1:
        print("You are genius" )
        break
    else:
        print("Try one more time!")


