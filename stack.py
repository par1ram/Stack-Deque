class Stack:
    def __init__(self):
        self._list = list()

    def push(self, element):
        self._list.append(element)
        return element

    def get(self):
        if len(self._list) == 0:
            pass
        else:
            return self._list.pop()

    def is_empty(self) -> bool:
        return len(self._list) == 0

    def len(self):
        return self._list.count(int)


file = open("scobki.txt", encoding='utf-8')
text = file.read()
file.close()


# Задание №4
def balance(txt):
    stack = Stack()
    flag = True
    for el in txt:
        if el == "(":
            stack.push(el)
        elif el == ")":
            if stack.is_empty():
                flag = False
                break
            else:
                el_steck = stack.get()
                if el_steck == '(' and el == ')':
                    continue

            flag = False
            break

    if flag and stack.is_empty():
        print("ЗАДАНИЕ№4(сортировка скобок):\nЭталон гармонии")
    else:
        print("ЗАДАНИЕ№4(сортировка скобок):\nБаланса не имеется")
    return


balance(text)

file = open("diski.txt", encoding='utf-8')
text1 = file.read()
file.close()


# Задание №3
def hanoi(txt):
    stack_i = Stack()
    stack_k = Stack()
    stack_tmp = Stack()

    for i in range(len(txt)):
        stack_i.push(int(txt[i]))

    def move_disk(source, destination):
        disk = source.get()
        destination.push(disk)

    def hanoi_helper(n, source, destination, temp):
        if n == 1:
            move_disk(source, destination)  # Крайний случай
        else:
            hanoi_helper(n-1, source, temp, destination)  # n-1 дисков на временный столбик
            move_disk(source, destination)  # n-ый, который самый большой диск на необходимый столбик
            hanoi_helper(n-1, temp, destination, source)  # n-1 дисков поверх самого большого

    # Вызываем рекурсивную функцию для перемещения дисков
    hanoi_helper(len(txt), stack_i, stack_k, stack_tmp)
    print("ЗАДАНИЕ №3:\nStack K:", stack_k._list)


hanoi(text1)

file = open("symbols.txt", encoding='utf-8')
text2 = file.read()
file.close()


# Задание №6
def print_symbols_in_order(txt):
    digits_stack = Stack()
    letters_stack = Stack()
    others_stack = Stack()

    for char in txt:
        if char.isdigit():
            digits_stack.push(char)
        elif char.isalpha():
            letters_stack.push(char)
        else:
            others_stack.push(char)

    print("ЗАДАНИЕ №6:\nЧисла:")
    digits = []
    while not digits_stack.is_empty():
        digits.append(digits_stack.get())
    print(*reversed(digits))

    print("\nБуквы:")
    letters = []
    while not letters_stack.is_empty():
        letters.append(letters_stack.get())
    print(*reversed(letters))

    print("\nОстальные символы:")
    others = []
    while not others_stack.is_empty():
        others.append(others_stack.get())
    print(*reversed(others))


print_symbols_in_order(text2)

file = open("old_text.txt", encoding='utf-8')
text3 = file.readlines()
file.close()


# Задание №8
def reverse_lines_and_save_to_file(lines, output_file):
    stack = Stack()
    for line in lines:
        stack.push(line.strip())
    with open(output_file, "w", encoding="utf-8") as output:
        while not stack.is_empty():
            output.write(stack.get() + "\n")


reverse_lines_and_save_to_file(text3, "reversed_text.txt")
