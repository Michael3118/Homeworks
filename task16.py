#task1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}. Nice to meet you!"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying hard."

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        return f"{self.name} is teaching."

# Examples of usage:
person = Person("John Doe", 30)
print(person.greet())  # Output: "Hello, my name is John Doe. Nice to meet you!"

student = Student("Alice", 20, "S001")
print(student.study())  # Output: "Alice is studying hard."
print(student.greet())  # Inherited from Person class

teacher = Teacher("Mr. Smith", 35, 50000)
print(teacher.teach())  # Output: "Mr. Smith is teaching."
print(teacher.greet())  # Inherited from Person class

#task2

class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums if num <= 0]

    def filter_leaps(self, dates):
        return [year for year in dates if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

#task3

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        self.products[product.name] = {'product': product, 'amount': amount, 'price': product.price * 1.3}

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_name, info in self.products.items():
            if info['product'].__dict__[identifier_type] == identifier:
                info['price'] -= info['price'] * percent / 100

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                return self.products[product_name]['price'] * amount
            else:
                raise ValueError("Not enough amount in stock")
        else:
            raise ValueError("Product not available")

    def get_income(self):
        return sum(info['price'] * info['amount'] for info in self.products.values())

    def get_all_products(self):
        return {name: (info['product'].type, info['product'].price, info['amount']) for name, info in self.products.items()}

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError("Product not available")

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)

#task4

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(f"Error: {msg}\n")
