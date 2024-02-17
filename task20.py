#task1
import unittest
def in_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

# Example usage:
for number in in_range(1, 10, 2):
    print(number)



class TestInRangeFunction(unittest.TestCase):

    def test_default_step(self):
        result = list(in_range(1, 5))
        self.assertEqual(result, [1, 2, 3, 4])

    def test_with_step(self):
        result = list(in_range(1, 10, 2))
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_negative_values(self):
        result = list(in_range(-5, 0, 2))
        self.assertEqual(result, [-5, -3, -1])

    def test_empty_range(self):
        result = list(in_range(10, 5))
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

#task2

class Phonebook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def lookup_contact(self, name):
        return self.contacts.get(name)

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()
        self.phonebook.add_contact("John", "123456789")
        self.phonebook.add_contact("Alice", "987654321")

    def test_lookup_existing_contact(self):
        result = self.phonebook.lookup_contact("John")
        self.assertEqual(result, "123456789")

    def test_lookup_nonexistent_contact(self):
        result = self.phonebook.lookup_contact("Bob")
        self.assertIsNone(result)

    def test_add_contact(self):
        self.phonebook.add_contact("Charlie", "555555555")
        result = self.phonebook.lookup_contact("Charlie")
        self.assertEqual(result, "555555555")

if __name__ == '__main__':
    unittest.main()

