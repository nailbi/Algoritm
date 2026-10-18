import random
import sys
import time

sys.setrecursionlimit(100000)

N = 10000


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def quick_sort(a, low=0, high=None):
    if high is None:
        high = len(a) - 1
    while low < high:
       
        pivot = a[(low + high) // 2]
        i, j = low, high
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        
        if j - low < high - i:
            quick_sort(a, low, j)
            low = i
        else:
            quick_sort(a, i, high)
            high = j
    return a


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    
    original = [random.randint(-100000, 100000) for _ in range(N)]
    expected = sorted(original)

    algorithms = [
        ("Пузырьковая", bubble_sort),
        ("Выбором", selection_sort),
        ("Вставками", insertion_sort),
        ("Быстрая", quick_sort),
        ("Слиянием", merge_sort),
    ]

    print(f"Размер массива: {N}")
    print(f"Первые 10 элементов: {original[:10]}\n")

    results = []
    for name, func in algorithms:
        data = original.copy()  
        start = time.perf_counter()
        sorted_data = func(data)
        elapsed = time.perf_counter() - start
        ok = sorted_data == expected
        results.append((name, elapsed))
        print(f"{name:<12} {elapsed:10.4f} с   {'OK' if ok else 'ОШИБКА'}")

    print("\nРейтинг (от быстрой к медленной):")
    for place, (name, elapsed) in enumerate(sorted(results, key=lambda r: r[1]), 1):
        print(f"{place}. {name:<12} {elapsed:.4f} с")


if __name__ == "__main__":
    main()
