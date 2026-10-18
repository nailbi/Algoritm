

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


def lower_bound(arr, x):
    
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, x):
    """Первый индекс, где arr[i] > x."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_search_all(arr, x):
    return list(range(lower_bound(arr, x), upper_bound(arr, x)))


def insert_sorted(arr, x):
    pos = upper_bound(arr, x)
    arr.insert(pos, x)
    return pos


def delete_all_sorted(arr, x):
    left = lower_bound(arr, x)
    right = upper_bound(arr, x)
    del arr[left:right]
    return right - left


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    n = read_int("Размер массива: ", 1)
    mode = input("Заполнить вручную (1) или случайно (2)? ").strip()
    if mode == "1":
        print("Вводите элементы (в любом порядке, массив будет упорядочен):")
        arr = [read_int(f"  элемент {i + 1}: ") for i in range(n)]
    else:
        arr = [random.randint(0, 99) for _ in range(n)]
    insertion_sort(arr)
    show(arr, "Упорядоченный массив")

    while True:
        print("\n1 - линейный поиск  2 - бинарный поиск  3 - вставка  "
              "4 - удаление  0 - выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            x = read_int("Искомое значение: ")
            idx = linear_search_all(arr, x)
            print(f"Линейный поиск: {idx if idx else 'не найдено'}")
            show(arr)
        elif choice == "2":
            x = read_int("Искомое значение: ")
            idx = binary_search_all(arr, x)
            print(f"Бинарный поиск: {idx if idx else 'не найдено'}")
            show(arr)
        elif choice == "3":
            x = read_int("Значение для вставки: ")
            pos = insert_sorted(arr, x)
            print(f"Значение {x} вставлено на позицию {pos}.")
            show(arr)
        elif choice == "4":
            x = read_int("Значение для удаления (все вхождения): ")
            removed = delete_all_sorted(arr, x)
            print(f"Удалено элементов: {removed}")
            show(arr)
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()