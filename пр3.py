import random


def generate_array(length, min_val, max_val):
    """
    Генерує масив заданої довжини в заданому діапазоні [min_val, max_val].
    """
    return [random.randint(min_val, max_val) for _ in range(length)]


def print_array(arr):
    """
    Виводить елементи масиву у вигляді:
    "{[cell - 0, value - 4], [cell - 2, value - 10]...[cell - n, value - n]}"
    """
    formatted_elements = [f"[cell - {i}, value - {val}]" for i, val in enumerate(arr)]
    print("{" + ", ".join(formatted_elements) + "}")


def bubble_sort(arr, ascending=True):
    """
    Сортування бульбашкою (Bubble sort).
    ascending=True: прямому порядку (від меншого до більшого)
    ascending=False: у зворотньому порядку (від більшого до меншого)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                condition = arr_copy[j] > arr_copy[j + 1]
            else:
                condition = arr_copy[j] < arr_copy[j + 1]

            if condition:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy


def insertion_sort(arr, ascending=True):
    """
    Сортування вставками (Insertion sort).
    """
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        if ascending:
            while j >= 0 and arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
        else:
            while j >= 0 and arr_copy[j] < key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
        arr_copy[j + 1] = key
    return arr_copy


def selection_sort(arr, ascending=True):
    """
    Сортування вибором (Selection sort).
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if ascending:
                if arr_copy[j] < arr_copy[target_idx]:
                    target_idx = j
            else:
                if arr_copy[j] > arr_copy[target_idx]:
                    target_idx = j
        arr_copy[i], arr_copy[target_idx] = arr_copy[target_idx], arr_copy[i]
    return arr_copy


# --- Демонстрація роботи алгоритмів ---
if __name__ == "__main__":
    # 1. Генерація початкового масиву
    original_array = generate_array(length=7, min_val=1, max_val=20)

    print("Початковий масив:")
    print_array(original_array)
    print("-" * 60)

    # 2. Bubble Sort
    print("Bubble Sort (прямий порядок - True):")
    print_array(bubble_sort(original_array, True))

    print("Bubble Sort (зворотний порядок - False):")
    print_array(bubble_sort(original_array, False))
    print("-" * 60)

    # 3. Insertion Sort
    print("Insertion Sort (прямий порядок - True):")
    print_array(insertion_sort(original_array, True))

    print("Insertion Sort (зворотний порядок - False):")
    print_array(insertion_sort(original_array, False))
    print("-" * 60)

    # 4. Selection Sort
    print("Selection Sort (прямий порядок - True):")
    print_array(selection_sort(original_array, True))

    print("Selection Sort (зворотний порядок - False):")
    print_array(selection_sort(original_array, False))
    print("-" * 60)