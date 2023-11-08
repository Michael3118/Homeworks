#task1
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

#task2
def stop_words(words):
    def decorator(func):
        def wrapper(name):
            modified_name = func(name)
            for word in words:
                modified_name = modified_name.replace(word, '*')
            return modified_name
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

#task3

def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(name):
            if not isinstance(name, type_):
                print(f"Failed: Argument is not of type {type_}")
                return False

            if len(name) > max_length:
                print(f"Failed: Argument length exceeds {max_length}")
                return False

            if not all(symbol in name for symbol in contains):
                print(f"Failed: Argument does not contain all symbols from {contains}")
                return False

            return func(name)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
