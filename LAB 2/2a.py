

import random


def read_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if min_value is not None and value < min_value:
            print(f"Ошибка: число должно быть не меньше {min_value}.")
            continue
        return value


def show(arr, title="Массив"):
    if len(arr) <= 100:
        print(f"{title} ({len(arr)} эл.): {arr}")
    else:
        print(f"{title} ({len(arr)} эл.): {arr[:20]} ... {arr[-20:]}")


def linear_search_all(arr, x):
    result = []
    for i in range(len(arr)):
        if arr[i] == x:
            result.append(i)
    return result


def insert_unsorted(arr, x):
    arr.append(x)


def delete_all_unsorted(arr, x):
    j = 0
    for i in range(len(arr)):
        if arr[i] != x:
            arr[j] = arr[i]
            j += 1
    removed = len(arr) - j
    del arr[j:]
    return removed


def main():
    n = read_int("Размер массива: ", 1)
    arr = [random.randint(0, 99) for _ in range(n)]
    show(arr, "Исходный массив")

    while True:
        print("\n1 - линейный поиск  2 - вставка  3 - удаление  0 - выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            x = read_int("Искомое значение: ")
            idx = linear_search_all(arr, x)
            if idx:
                print(f"Значение {x} найдено на позициях (с 0): {idx}")
            else:
                print(f"Значение {x} не найдено.")
            show(arr)
        elif choice == "2":
            x = read_int("Значение для вставки: ")
            insert_unsorted(arr, x)
            print(f"Значение {x} добавлено в конец массива.")
            show(arr)
        elif choice == "3":
            x = read_int("Значение для удаления (все вхождения): ")
            removed = delete_all_unsorted(arr, x)
            print(f"Удалено элементов: {removed}")
            show(arr)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()