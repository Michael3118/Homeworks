#task1

def word_frequency(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?").lower()
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

input_sentence = input("Enter a sentence: ")
result = word_frequency(input_sentence)

print(result)


#task2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

# Iterate through the items in the stock and calculate the total price
for item in stock:
    if item in prices:  # Check if the item has a defined price
        total_price += stock[item] * prices[item]

# Print the total price
print("Total Price of Stock: ${:.2f}".format(total_price))

#task3

result = [(i, i ** 2) for i in range(1, 11)]
print(result)

#task4

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekdays_dict = {i + 1: day for i, day in enumerate(weekdays)}
reverse_weekdays_dict = {day: i + 1 for i, day in enumerate(weekdays)}

print("Словник виду:")
print(weekdays_dict)

print("\nЗворотний словник:")
print(reverse_weekdays_dict)