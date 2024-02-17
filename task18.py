#task1

import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def validate(cls, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

if __name__ == "__main__":
    try:
        User.validate("invalid_email")  # This will raise a ValueError
    except ValueError as e:
        print(e)

    user = User("John", "john@example.com")  # This will not raise an error


#task2

class Boss:
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            raise ValueError("Can only add instances of Worker to workers list")


class Worker:
    def __init__(self, id_, name, company, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  # using the setter

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss) or new_boss is None:
            self._boss = new_boss
            if new_boss is not None:
                new_boss.add_worker(self)
        else:
            raise ValueError("Value should be an instance of Boss or None")


# Example Usage:
if __name__ == "__main__":
    boss1 = Boss(1, "John", "ABC Company")
    boss2 = Boss(2, "Alice", "XYZ Company")

    worker1 = Worker(101, "Mike", "ABC Company", boss1)
    worker2 = Worker(102, "Emma", "XYZ Company")

    try:
        worker2.boss = boss2  # This will raise a ValueError
    except ValueError as e:
        print(e)

    worker3 = Worker(103, "Chris", "ABC Company")
    worker3.boss = boss1  # This will set worker3's boss to boss1 and add worker3 to boss1's workers list

#task3

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper

# Example Usage
@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True
