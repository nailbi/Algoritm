OPEN = "([{"
CLOSE = ")]}"
PAIRS = {")": "(", "]": "[", "}": "{"}


def only_brackets(s):
  
    return "".join(ch for ch in s if ch in OPEN or ch in CLOSE)


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
  

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        node = Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek пустой очереди")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size


class ReverseQueue:
    # противоположно направленная очередь: элементы встают в голову,
    # поэтому первым выходит последний добавленный

    def __init__(self):
        self._head = None
        self._size = 0

    def enqueue(self, value):
        self._head = Node(value, self._head)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek пустой очереди")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size


def check_with_queue(s):
    # основная очередь хранит скобки строки, обратная — открытые скобки
    brackets = only_brackets(s)
    if not brackets:
        return None

    queue = Queue()
    for ch in brackets:
        queue.enqueue(ch)

    opened = ReverseQueue()
    while not queue.is_empty():
        ch = queue.dequeue()
        if ch in OPEN:
            opened.enqueue(ch)
        elif opened.is_empty() or opened.dequeue() != PAIRS[ch]:
            return False

    return opened.is_empty()


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
        assert check_with_queue(s) == expected, f"тест не прошёл: {s!r}"

    while True:
        try:
            s = input("Введите строку (пустой ввод — выход): ")
        except EOFError:
            break
        if not s:
            break
        print("  Скобки:", only_brackets(s) or "—")
        print("  Очередь:", result(check_with_queue(s)))


if __name__ == "__main__":
    main()
