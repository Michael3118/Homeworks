#task1
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")


# Example usage:
person = Person("Carl", "Johnson", 26)
person.talk()

#task2

class Dog:
    age_factor = 7  # Class attribute

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor

# Example usage:
dog = Dog(5)  # Creating a Dog instance with age 5
human_equivalent_age = dog.human_age()  # Getting the human equivalent age
print(f"The dog's age in human years is {human_equivalent_age}")

#task3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current = 0

    def first_channel(self):
        self.current = 0
        return self.channels[self.current]

    def last_channel(self):
        self.current = len(self.channels) - 1
        return self.channels[self.current]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current = N - 1
            return self.channels[self.current]

    def next_channel(self):
        self.current = (self.current + 1) % len(self.channels)
        return self.channels[self.current]

    def previous_channel(self):
        self.current = (self.current - 1) % len(self.channels)
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]

    def exists(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        else:
            return "Yes" if channel in self.channels else "No"

# Example usage:
controller = TVController(CHANNELS)
print(controller.first_channel())  # Output: "BBC"
print(controller.last_channel())  # Output: "TV1000"
print(controller.turn_channel(1))  # Output: "BBC"
print(controller.next_channel())  # Output: "Discovery"
print(controller.previous_channel())  # Output: "BBC"
print(controller.current_channel())  # Output: "BBC"
print(controller.exists(4))  # Output: "No"
print(controller.exists("BBC"))  # Output: "Yes"
