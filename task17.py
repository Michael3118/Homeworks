#task1

class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "woof woof"

class Cat(Animal):
    def talk(self):
        return "meow"

def perform_talk(animal_instance):
    return animal_instance.talk()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using the perform_talk function with instances of Dog and Cat
print(perform_talk(dog))  # Output: "woof woof"
print(perform_talk(cat))  # Output: "meow"


#task2

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"Book: {self.name}, {self.year}, {self.author}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"Author: {self.name}, {self.country}, {self.birthday}"


#task3

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result = x + y
    print(result)  # Output: 3/4
