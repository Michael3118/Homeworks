#task1

def favourite_movie(name):
    print("My favorite film is " + name)

favourite_movie("Hungry Games")

#task2

def make_country(country_name, country_capital):
    return {'name': country_name, 'capital': country_capital}

name = input("Enter the country's name: ")
capital = input("Enter the country's capital: ")

country_dict = make_country(name, capital)
print(country_dict)

#task3

def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        return args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return None

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))