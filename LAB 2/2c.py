

import random
import time


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


def insert_sorted(arr, x):
    arr.insert(upper_bound(arr, x), x)


def delete_all_sorted(arr, x):
    left = lower_bound(arr, x)
    right = upper_bound(arr, x)
    del arr[left:right]
    return right - left


def measure(func, repeats, prepare=None):
    total = 0.0
    for _ in range(repeats):
        args = prepare() if prepare else ()
        start = time.perf_counter()
        func(*args)
        total += time.perf_counter() - start
    return total / repeats


def fmt(seconds):
    return f"{seconds * 1e6:12.2f} мкс"


def main():
    n = read_int("Количество элементов (не менее 10000): ", 10000)
    value_range = max(10, n // 10)  
    unsorted_arr = [random.randint(0, value_range) for _ in range(n)]
    sorted_arr = unsorted_arr[:]
    sorted_arr.sort()  
    print(f"Сгенерирован массив из {n} элементов со значениями 0..{value_range}.")

    x = read_int("Значение для поиска / вставки / удаления: ")
    print("Измерение, подождите...")

    r_lin_u = measure(lambda: linear_search_all(unsorted_arr, x), 50)
    r_lin_s = measure(lambda: linear_search_all(sorted_arr, x), 50)
    r_bin_s = measure(lambda: binary_search_all(sorted_arr, x), 2000)

    r_ins_u = measure(lambda a: insert_unsorted(a, x), 50,
                      lambda: (unsorted_arr[:],))
    r_ins_s = measure(lambda a: insert_sorted(a, x), 50,
                      lambda: (sorted_arr[:],))

    r_del_u = measure(lambda a: delete_all_unsorted(a, x), 50,
                      lambda: (unsorted_arr[:],))
    r_del_s = measure(lambda a: delete_all_sorted(a, x), 50,
                      lambda: (sorted_arr[:],))

   
    print(f"\nРезультаты (среднее время одной операции, n = {n}):")
  
    print(f"{'Операция':<38}{'Время':>24}")
 
    print(f"{'Поиск: линейный, неупорядоченный':<38}{fmt(r_lin_u):>24}")
    print(f"{'Поиск: линейный, упорядоченный':<38}{fmt(r_lin_s):>24}")
    print(f"{'Поиск: бинарный, упорядоченный':<38}{fmt(r_bin_s):>24}")
   
    print(f"{'Вставка: неупорядоченный':<38}{fmt(r_ins_u):>24}")
    print(f"{'Вставка: упорядоченный':<38}{fmt(r_ins_s):>24}")
  
    print(f"{'Удаление: неупорядоченный':<38}{fmt(r_del_u):>24}")
    print(f"{'Удаление: упорядоченный':<38}{fmt(r_del_s):>24}")
   
    if r_bin_s > 0:
        print(f"Бинарный поиск быстрее линейного (упорядоченный массив) "
              f"примерно в {r_lin_s / r_bin_s:.0f} раз.")


if __name__ == "__main__":
    main()