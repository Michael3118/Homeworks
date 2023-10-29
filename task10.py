#task1
def oops():
    print(10/0)
    names = {"Michael", "John", "Jack"}
    names = ["Bill"]
try:
    oops()
except ZeroDivisionError:
    print("Index Error, impossible action")

#task2
def calculate_squared_division():
    try:
        a = float(input("Enter number a: "))
        b = float(input("Enter number b: "))

        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = (a ** 2) / b
        return print("The result of squared division is ", result)

    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)

# Function call
calculate_squared_division()


