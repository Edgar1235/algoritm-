import random


# --- Допоміжні функції (з зображення) ---

def generate_array(length: int, min_val: int, max_val: int) -> list:
    """Генерує масив заданої довжини в діапазоні [min_val, max_val]"""
    return [random.randint(min_val, max_val) for _ in range(length)]


def print_array(arr: list):
    """Форматований вивід елементів масиву"""
    formatted_elements = [f"[елемент_{i + 1}_значення_{val}]" for i, val in enumerate(arr)]
    print(",\n".join(formatted_elements))
    print()


# --- Методи завдань ---

# 1. Порахувати кількість та суму парних елементів масиву в діапазоні
def task1_count_and_sum_even_in_range(arr: list, min_val: int, max_val: int):
    filtered = [x for x in arr if x % 2 == 0 and min_val <= x <= max_val]
    count = len(filtered)
    total_sum = sum(filtered)
    print(f"[Завдання 1] У діапазоні [{min_val}, {max_val}] парних елементів: {count}, їх сума: {total_sum}")


# 2. Середнє арифметичне та кількість елементів, більших за нього
def task2_average_and_greater_count(arr: list):
    if not arr:
        return
    avg = sum(arr) / len(arr)
    greater_count = sum(1 for x in arr if x > avg)
    print(f"[Завдання 2] Середнє арифметичне: {avg:.2f}, кількість елементів > avg: {greater_count}")


# 3. Третій масив як попарна сума двох масивів однакової довжини
def task3_pairwise_sum(arr1: list, arr2: list) -> list:
    return [a + b for a, b in zip(arr1, arr2)]


# 4. Третій масив як конкатенація двох масивів різної довжини
def task4_concat_arrays(arr1: list, arr2: list) -> list:
    return arr1 + arr2


# 5. Поміняти місцями максимум та мінімум
def task5_swap_min_max(arr: list) -> list:
    if not arr:
        return arr
    res = arr.copy()
    min_idx = res.index(min(res))
    max_idx = res.index(max(res))
    res[min_idx], res[max_idx] = res[max_idx], res[min_idx]
    return res


# 6. Поділити масив на два: з додатних та від’ємних елементів
def task6_split_positive_negative(arr: list):
    positive = [x for x in arr if x > 0]
    negative = [x for x in arr if x < 0]
    print("Додатні елементи:")
    print_array(positive)
    print("Від’ємні елементи:")
    print_array(negative)


# 7. Видалити дублікати максимума та мінімума
def task7_remove_min_max_duplicates(arr: list) -> list:
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)

    first_max_found = False
    first_min_found = False
    result = []

    for item in arr:
        if item == max_val:
            if not first_max_found:
                result.append(item)
                first_max_found = True
        elif item == min_val:
            if not first_min_found:
                result.append(item)
                first_min_found = True
        else:
            result.append(item)

    return result


# 8. Третій масив з елементів двох масивів в межах між значеннями їх середніх арифметичних
def task8_elements_between_averages(arr1: list, arr2: list) -> list:
    avg1 = sum(arr1) / len(arr1)
    avg2 = sum(arr2) / len(arr2)

    lower_bound = min(avg1, avg2)
    upper_bound = max(avg1, avg2)

    combined = arr1 + arr2
    return [x for x in combined if lower_bound <= x <= upper_bound]


# --- Демонстрація роботи ---
if __name__ == "__main__":
    array1 = generate_array(10, -50, 50)
    array2 = generate_array(10, -50, 50)
    array3 = generate_array(5, -20, 20)

    print("--- Початковий масив 1 ---")
    print_array(array1)

    task1_count_and_sum_even_in_range(array1, -20, 20)
    task2_average_and_greater_count(array1)

    print("\n--- Завдання 3: Попарна сума ---")
    print_array(task3_pairwise_sum(array1, array2))

    print("\n--- Завдання 4: Конкатенація ---")
    print_array(task4_concat_arrays(array1, array3))

    print("\n--- Завдання 5: Обмін Min та Max ---")
    print_array(task5_swap_min_max(array1))

    print("\n--- Завдання 6: Додатні та від'ємні ---")
    task6_split_positive_negative(array1)

    print("\n--- Завдання 7: Видалення дублікатів Min/Max ---")
    test_duplicates = [5, 10, -3, 10, -3, 2, 10]
    print("Тестовий масив:")
    print_array(test_duplicates)
    print("Після чистки:")
    print_array(task7_remove_min_max_duplicates(test_duplicates))

    print("\n--- Завдання 8: Елементи між середніми арифметичними ---")
    print_array(task8_elements_between_averages(array1, array2))