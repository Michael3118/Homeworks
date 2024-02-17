#task1
import unittest
import os
class CustomFileOpener:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open_count = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.open_count += 1
        print(f"File '{self.filename}' opened. Open count: {self.open_count}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' closed. Open count: {self.open_count}")

    def get_open_count(self):
        return self.open_count

    def log_operation(self, message):
        print(f"LOG: {message}")

# Example usage:
with CustomFileOpener('example.txt', 'w') as file:
    file.write('Hello, world!')

with CustomFileOpener('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Accessing additional functionality
file_opener = CustomFileOpener('example.txt')
file_opener.log_operation('Performed some operation')
print(f"Total open count: {file_opener.get_open_count()}")


#task2
class TestCustomFileOpener(unittest.TestCase):

    def setUp(self):
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as file:
            file.write("Test content")

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_file_read(self):
        with CustomFileOpener(self.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "Test content")

    def test_file_write(self):
        with CustomFileOpener(self.filename, 'a') as file:
            file.write("\nAdditional content")

        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "Test content\nAdditional content")

    def test_open_count(self):
        file_opener = CustomFileOpener(self.filename)
        with file_opener as file1:
            self.assertEqual(file_opener.get_open_count(), 1)

        with file_opener as file2:
            self.assertEqual(file_opener.get_open_count(), 2)

    def test_log_operation(self):
        file_opener = CustomFileOpener(self.filename)
        with file_opener as file:
            file_opener.log_operation("Test log message")

    def test_nonexistent_file(self):
        nonexistent_filename = 'nonexistent_file.txt'
        with self.assertRaises(FileNotFoundError):
            with CustomFileOpener(nonexistent_filename, 'r') as file:
                pass

if __name__ == '__main__':
    unittest.main()

#task3
# main_module.py
def process_file(file_obj):
    content = file_obj.read()
    return content.upper()
# test_main_module.py
import pytest
@pytest.fixture
def sample_file():
    content = "Hello, this is a sample text."
    filename = 'sample_file.txt'

    with open(filename, 'w') as file:
        file.write(content)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)

def test_process_file(sample_file):
    with CustomFileOpener(sample_file, 'r') as file_obj:
        result = process_file(file_obj)

    assert result == "HELLO, THIS IS A SAMPLE TEXT."
