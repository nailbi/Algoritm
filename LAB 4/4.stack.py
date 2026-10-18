OPEN = "([{"
CLOSE = ")]}"
PAIRS = {")": "(", "]": "[", "}": "{"}


def only_brackets(s):
    
    return "".join(ch for ch in s if ch in OPEN or ch in CLOSE)


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        self._top = Node(value, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek пустого стека")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size


def check_with_stack(s):
   
    brackets = only_brackets(s)
    if not brackets:
        return None

    stack = Stack()
    for ch in brackets:
        if ch in OPEN:
            stack.push(ch)
        else:
            if stack.is_empty() or stack.pop() != PAIRS[ch]:
                return False
    return stack.is_empty()


def result(ok):
    if ok is None:
        return "ошибка: в строке нет скобок"
    return "скобки парные" if ok else "скобки НЕ парные"


def main():
  
    tests = [
        ("()", True),
        ("([]{})", True),
        ("{[()()]}", True),
        ("(", False),
        (")(", False),
        ("([)]", False),
        ("(()", False),
        ("{[}]", False),
        ("(1+2)*[3]", True),
        ("(a)", True),
        ("(а[б]в)", True),
        ("a*(b+c)-[d/{e+f}]", True),
        ("if (a[i] > b) { c(); }", True),
        ("1(2", False),
        ("x)y(", False),
        ("{слово(word]}", False),
        ("", None),
        ("123", None),
        ("abc", None),
        ("a + b = 5", None),
    ]
    for s, expected in tests:
        assert check_with_stack(s) == expected, f"тест не прошёл: {s!r}"

    while True:
        try:
            s = input("Введите строку (пустой ввод — выход): ")
        except EOFError:
            break
        if not s:
            break
        print("  Скобки:", only_brackets(s) or "—")
        print("  Стек:", result(check_with_stack(s)))


if __name__ == "__main__":
    main()
