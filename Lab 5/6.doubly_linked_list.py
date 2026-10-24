class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    # Двусвязный список: каждый узел хранит ссылки на предыдущий и следующий

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value
            node = node.next

    def reversed(self):
        node = self._tail
        while node is not None:
            yield node.value
            node = node.prev

    def __str__(self):
        if self._head is None:
            return "[] (пусто)"
        return "None <-> " + " <-> ".join(str(v) for v in self) + " <-> None"

    def _check_index(self, index, upper):
        if not 0 <= index <= upper:
            raise IndexError(f"индекс {index} вне диапазона 0..{upper}")

    def _node_at(self, index):
   
        if index < self._size // 2:
            node = self._head
            for _ in range(index):
                node = node.next
        else:
            node = self._tail
            for _ in range(self._size - 1 - index):
                node = node.prev
        return node

    def _find_node(self, value):
        node, index = self._head, 0
        while node is not None and node.value != value:
            node, index = node.next, index + 1
        return node, index

    def _insert_before(self, node, value):
        
        if node is None:
            new = Node(value, self._tail, None)
            if self._tail is None:
                self._head = new
            else:
                self._tail.next = new
            self._tail = new
        else:
            new = Node(value, node.prev, node)
            if node.prev is None:
                self._head = new
            else:
                node.prev.next = new
            node.prev = new
        self._size += 1

    def _unlink(self, node):
        if node.prev is None:
            self._head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self._tail = node.prev
        else:
            node.next.prev = node.prev
        self._size -= 1
        return node.value

    #вставка

    def insert_at(self, index, value):
       
        self._check_index(index, self._size)
        target = None if index == self._size else self._node_at(index)
        self._insert_before(target, value)

    def insert_after_value(self, target, value):
        
        node, _ = self._find_node(target)
        if node is None:
            raise ValueError(f"значение {target!r} не найдено")
        self._insert_before(node.next, value)

    def append(self, value):
        self._insert_before(None, value)

    # удаление

    def remove_at(self, index):
        
        self._check_index(index, self._size - 1)
        return self._unlink(self._node_at(index))

    def remove_value(self, value):
        
        node, index = self._find_node(value)
        if node is None:
            raise ValueError(f"значение {value!r} не найдено")
        self._unlink(node)
        return index

    def remove_all(self, value):

        removed = []
        node, index = self._head, 0
        while node is not None:
            next_node = node.next
            if node.value == value:
                self._unlink(node)
                removed.append(index)
            node, index = next_node, index + 1
        if not removed:
            raise ValueError(f"значение {value!r} не найдено")
        return removed

    #поиск

    def get(self, index):
       
        self._check_index(index, self._size - 1)
        return self._node_at(index).value

    def find(self, value):
       
        node, index = self._find_node(value)
        return -1 if node is None else index

    def find_all(self, value):

        return [index for index, v in enumerate(self) if v == value]


def parse_value(s):
    
    s = s.strip()
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


def read_index(prompt):
    return int(input(prompt).strip())


MENU = """
Двусвязный список
  1 — вставить по индексу
  2 — вставить после значения
  3 — удалить по индексу
  4 — удалить по значению
  5 — найти по индексу
  6 — найти по значению
  7 — показать список (вперёд и назад)
  0 — выход"""


def main():
    lst = DoublyLinkedList()
    for v in (10, 20, 30):
        lst.append(v)

    
    t = DoublyLinkedList()
    t.insert_at(0, 1); t.insert_at(1, 3); t.insert_at(1, 2); t.insert_at(0, 0)
    assert list(t) == [0, 1, 2, 3] and list(t.reversed()) == [3, 2, 1, 0]
    t.insert_after_value(3, 4)
    assert list(t) == [0, 1, 2, 3, 4]
    assert t.remove_at(0) == 0 and t.remove_at(3) == 4
    assert t.remove_value(2) == 1 and list(t) == [1, 3]
    assert list(t.reversed()) == [3, 1]
    assert t.find(3) == 1 and t.find(99) == -1 and t.get(1) == 3
    t.append(1)
    assert t.find_all(1) == [0, 2] and t.find_all(99) == []
    assert t.remove_all(1) == [0, 2] and list(t) == [3] and len(t) == 1
    assert list(t.reversed()) == [3]

    print("Начальный список:", lst)
    while True:
        print(MENU)
        try:
            choice = input("Выбор: ").strip()
        except EOFError:
            break
        try:
            if choice == "1":
                index = read_index(f"Индекс (0..{len(lst)}): ")
                value = parse_value(input("Значение: "))
                lst.insert_at(index, value)
                print(f"Вставлено {value!r} на позицию {index}")
            elif choice == "2":
                target = parse_value(input("После какого значения вставить: "))
                value = parse_value(input("Новое значение: "))
                lst.insert_after_value(target, value)
                print(f"Вставлено {value!r} после {target!r}")
            elif choice == "3":
                index = read_index(f"Индекс (0..{len(lst) - 1}): ")
                print(f"Удалено значение {lst.remove_at(index)!r} с позиции {index}")
            elif choice == "4":
                value = parse_value(input("Значение: "))
                positions = lst.remove_all(value)
                if len(positions) == 1:
                    print(f"Удалено {value!r} с позиции {positions[0]}")
                else:
                    print(f"Удалено {value!r} с позиций "
                          + ", ".join(str(i) for i in positions))
            elif choice == "5":
                index = read_index(f"Индекс (0..{len(lst) - 1}): ")
                print(f"Элемент [{index}] = {lst.get(index)!r}")
            elif choice == "6":
                value = parse_value(input("Значение: "))
                positions = lst.find_all(value)
                if not positions:
                    print(f"Значение {value!r} не найдено")
                elif len(positions) == 1:
                    print(f"Значение {value!r} найдено на позиции {positions[0]}")
                else:
                    print(f"Значение {value!r} найдено на позициях "
                          + ", ".join(str(i) for i in positions))
            elif choice == "7":
                print("Назад:", " <-> ".join(str(v) for v in lst.reversed()) or "—")
            elif choice == "0":
                break
            else:
                print("Неизвестная команда")
                continue
        except ValueError as e:
            print("Ошибка:", e if "значение" in str(e) else "введите целое число")
        except IndexError as e:
            print("Ошибка:", e)
        except EOFError:
            break
        print(f"Список ({len(lst)} эл.): {lst}")


if __name__ == "__main__":
    main()
