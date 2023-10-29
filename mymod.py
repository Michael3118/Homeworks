
def count_lines(name):
    with open(name, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

def count_chars(name):
    with open(name, 'r') as file:
        char_count = len(file.read())
    return char_count

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")

if __name__ == "__main__":
    test("mymod.py")
