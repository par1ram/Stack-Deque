from collections import deque


class Deque:
    def __init__(self):
        self._deque = deque()

    def append(self, element):
        self._deque.append(element)
        return element

    def appendleft(self, element):
        self._deque.appendleft(element)
        return element

    def pop(self):
        if len(self._deque) == 0:
            pass
        else:
            return self._deque.pop()

    def popleft(self):
        if len(self._deque) == 0:
            pass
        else:
            return self._deque.popleft()

    def is_empty(self) -> bool:
        return len(self._deque) == 0

    def __len__(self):
        return self._deque.count(int)


# Задание №1
def sort_books(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as books:
        q1 = Deque()
        q2 = Deque()
        for book in books:
            q1.append(book.strip())

        while q1:
            current_book = q1.pop()
            while not q2.is_empty() and q2.pop() > current_book:
                q1.appendleft(q2.popleft())
            q2.append(current_book)

    with open(output_file, 'w', encoding="utf-8") as sorted_books:
        while not q2.is_empty():
            sorted_books.write(q2.pop() + "\n")


sort_books('books.txt', 'sorted_books.txt')


# Задание №2
def decrypt_message(input_file):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    d = deque(alphabet)

    with open(input_file, 'r', encoding='utf-8') as file:
        encrypted_message = file.read()

    decrypted_message = ""
    for char in encrypted_message:
        if char.lower() in alphabet:
            char_lower = char.lower()
            for i, c in enumerate(alphabet):
                if c == char_lower:
                    next_char = d[(i + 2) % len(d)]
                    decrypted_message += next_char
                    break
        else:
            decrypted_message += char

    return decrypted_message


decrypted_text = decrypt_message('encrypted_message.txt')
print("ЗАДАНИЕ №2\n", decrypted_text)


# Задание №5
def check_brackets_balance(input_file):
    brackets_stack = Deque()
    flag = True

    with open(input_file, 'r') as file:
        program_code = file.read()

    for char in program_code:
        if char == '[':
            brackets_stack.append(char)
        elif char == ']':
            if brackets_stack.is_empty():
                flag = False
                break
            else:
                current_char = brackets_stack.pop()
                if current_char == '[' and char == ']':
                    continue

            flag = False
            break

    if flag and len(brackets_stack) == 0:
        print("ЗАДАНИЕ№5(сортировка квадратных скобок):\nЭталон гармонии")
    else:
        print("ЗАДАНИЕ№5(сортировка квадратных скобок):\nБаланса не имеется")


check_brackets_balance("program.txt")


# Задание №7
def print_numbers(input_file):
    negative_numbers = Deque()
    positive_numbers = Deque()

    with open(input_file, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            for num in numbers:
                num = int(num)
                if num < 0:
                    negative_numbers.appendleft(num)
                else:
                    positive_numbers.appendleft(num)

    print("ЗАДАНИЕ№7\nОтрицательные числа:")
    while not negative_numbers.is_empty():
        print(negative_numbers.pop())
    print(f"Положительные числа:")
    while not positive_numbers.is_empty():
        print(positive_numbers.pop())


print_numbers("numbers.txt")
