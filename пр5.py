import random
import sys
import time

# Збільшуємо ліміт рекурсії для роботи з великими масивами (наприклад, 100 000 елементів)
sys.setrecursionlimit(200000)


def partition(arr: list[float], low: int, high: int, reverse: bool = False) -> int:
    """Функція партиціювання (алгоритм Ломуто).

    Обирає останній елемент масиву як півоту та групує елементи.
    """
    pivot = arr[high]
    i = low - 1  # Індекс для елементів, що задовольняють умову

    for j in range(low, high):
        # Якщо reverse=False (за зростанням) -> шукаємо arr[j] <= pivot
        # Якщо reverse=True (за спаданням) -> шукаємо arr[j] >= pivot
        if (not reverse and arr[j] <= pivot) or (
            reverse and arr[j] >= pivot
        ):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Міняємо місцями півоту з елементом після останнього знайденого
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_recursive(
    arr: list[float], low: int, high: int, reverse: bool = False
) -> None:
    """Допоміжна рекурсивна функція QuickSort."""
    if low < high:
        pi = partition(arr, low, high, reverse)
        quick_sort_recursive(arr, low, pi - 1, reverse)
        quick_sort_recursive(arr, pi + 1, high, reverse)


def quick_sort(arr: list[float], reverse: bool = False) -> list[float]:
    """Головний метод QuickSort[cite: 1].

    :param arr: Масив дробових чисел[cite: 1]
    :param reverse: False - за зростанням, True - за спаданням[cite: 1]
    :return: Відсортований масив
    """
    quick_sort_recursive(arr, 0, len(arr) - 1, reverse)
    return arr


def is_sorted(arr: list[float], reverse: bool = False) -> bool:
    """Перевіряє, чи впорядкований масив[cite: 1].

    :param arr: Масив чисел[cite: 1]
    :param reverse: Напрямок сортування (False - зростання, True - спадання)[cite: 1]
    :return: True, якщо масив відсортований, інакше False[cite: 1]
    """
    for i in range(len(arr) - 1):
        if not reverse:
            if arr[i] > arr[i + 1]:
                return False
        else:
            if arr[i] < arr[i + 1]:
                return False
    return True


# --- Алгоритми з практичної роботи №3 (для порівняння) ---


def bubble_sort(arr: list[float], reverse: bool = False) -> list[float]:
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if (not reverse and arr_copy[j] > arr_copy[j + 1]) or (
                reverse and arr_copy[j] < arr_copy[j + 1]
            ):
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy


def selection_sort(arr: list[float], reverse: bool = False) -> list[float]:
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if (not reverse and arr_copy[j] < arr_copy[target_idx]) or (
                reverse and arr_copy[j] > arr_copy[target_idx]
            ):
                target_idx = j
        arr_copy[i], arr_copy[target_idx] = arr_copy[target_idx], arr_copy[i]
    return arr_copy


def insertion_sort(arr: list[float], reverse: bool = False) -> list[float]:
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and (
            (not reverse and arr_copy[j] > key)
            or (reverse and arr_copy[j] < key)
        ):
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy


# --- Тестування та порівняння продуктивності ---

if __name__ == "__main__":
    # 1. Демонстрація роботи на маленькому масиві з методички[cite: 1]
    sample_array = [3.0, 7.0, 0.0, 1.0, 4.0, 2.0]
    print(f"Початковий масив: {sample_array}")

    sorted_asc = quick_sort(sample_array.copy(), reverse=False)
    print(f"QuickSort (зростання): {sorted_asc}")
    print(f"Перевірка is_sorted: {is_sorted(sorted_asc, reverse=False)}")

    sorted_desc = quick_sort(sample_array.copy(), reverse=True)
    print(f"QuickSort (спадання): {sorted_desc}")
    print(f"Перевірка is_sorted: {is_sorted(sorted_desc, reverse=True)}\n")

    # 2. Тестування продуктивності для масивів різного розміру[cite: 1]
    sizes = [1_000, 10_000, 100_000]

    print("=" * 65)
    print(
        f"{'Розмір масиву':<15} | {'Алгоритм':<15} | {'Час виконання (сек)':<20}"
    )
    print("=" * 65)

    for size in sizes:
        # Генеруємо випадковий масив дробових чисел
        test_data = [random.uniform(-1000.0, 1000.0) for _ in range(size)]

        # --- QuickSort ---
        data_qs = test_data.copy()
        start = time.perf_counter()
        quick_sort(data_qs, reverse=False)
        end = time.perf_counter()
        time_qs = end - start
        print(f"{size:<15} | {'QuickSort':<15} | {time_qs:<20.5f}")

        # Алгоритми з ПР3 (О(N^2)) запускаємо тільки для розмірів <= 10 000,
        # щоб уникнути занадто тривалого очікування для 100 000.
        if size <= 10_000:
            # Bubble Sort
            data_bs = test_data.copy()
            start = time.perf_counter()
            bubble_sort(data_bs, reverse=False)
            end = time.perf_counter()
            print(f"{size:<15} | {'Bubble Sort':<15} | {end - start:<20.5f}")

            # Selection Sort
            data_ss = test_data.copy()
            start = time.perf_counter()
            selection_sort(data_ss, reverse=False)
            end = time.perf_counter()
            print(f"{size:<15} | {'Selection Sort':<15} | {end - start:<20.5f}")

            # Insertion Sort
            data_is = test_data.copy()
            start = time.perf_counter()
            insertion_sort(data_is, reverse=False)
            end = time.perf_counter()
            print(f"{size:<15} | {'Insertion Sort':<15} | {end - start:<20.5f}")
        else:
            print(
                f"{size:<15} | {'Алгоритми ПР№3':<15} | {'Пропущено (>10k)':<20}"
            )

        print("-" * 65)