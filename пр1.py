import random


# ==========================================
# ПІДГОТОВКА: Допоміжний метод
# ==========================================
def generate_array(length: int, min_val: int, max_val: int) -> list[int]:
    """Генерує список цілих випадкових чисел заданої довжини в заданому діапазоні."""
    return [random.randint(min_val, max_val) for _ in range(length)]


# ==========================================
# ОСНОВНІ ЗАВДАННЯ
# ==========================================

# 1. Кількість та сума парних елементів у заданому діапазоні індексів
def count_and_sum_evens_in_range(arr: list[int], start_idx: int, end_idx: int) -> tuple[int, int]:
    # Сріз масиву за заданими індексами включно з end_idx
    sub_arr = arr[start_idx:end_idx + 1]
    evens = [x for x in sub_arr if x % 2 == 0]
    return len(evens), sum(evens)


# 2. Середнє арифметичне та кількість елементів, більших за нього
def avg_and_count_greater(arr: list[int]) -> tuple[float, int]:
    if not arr:
        return 0.0, 0
    avg = sum(arr) / len(arr)
    count = sum(1 for x in arr if x > avg)
    return avg, count


# 3. Попарна сума двох масивів однакової довжини
def pair_sum(arr1: list[int], arr2: list[int]) -> list[int]:
    return [a + b for a, b in zip(arr1, arr2)]


# 4. Конкатенація двох масивів
def concatenate_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    return arr1 + arr2


# 5. Поміняти місцями максимум та мінімум
def swap_max_min(arr: list[int]) -> list[int]:
    if not arr:
        return []
    res = arr.copy()
    min_val, max_val = min(res), max(res)

    # Знаходимо перші входження елементів
    min_idx, max_idx = res.index(min_val), res.index(max_val)

    # Міняємо місцями
    res[min_idx], res[max_idx] = res[max_idx], res[min_idx]
    return res


# 6. Поділ на масиви додатних та від'ємних елементів
def split_positive_negative(arr: list[int]) -> tuple[list[int], list[int]]:
    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]
    return positives, negatives


# 7. Видалення дублікатів максимума та мінімума (залишається по одному кожному)
def remove_max_min_duplicates(arr: list[int]) -> list[int]:
    if not arr:
        return []
    min_val, max_val = min(arr), max(arr)

    res = []
    min_seen = False
    max_seen = False

    for x in arr:
        if x == min_val:
            if not min_seen:
                res.append(x)
                min_seen = True
        elif x == max_val:
            if not max_seen:
                res.append(x)
                max_seen = True
        else:
            res.append(x)

    return res


# 8. Третій масив з елементів, розташованих між середніми арифметичними двох масивів
def filter_between_averages(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1 or not arr2:
        return []
    avg1 = sum(arr1) / len(arr1)
    avg2 = sum(arr2) / len(arr2)

    lower_bound = min(avg1, avg2)
    upper_bound = max(avg1, avg2)

    combined = arr1 + arr2
    return [x for x in combined if lower_bound <= x <= upper_bound]


# ==========================================
# ДОДАТКОВЕ ЗАВДАННЯ: Симуляція інвентарю
# ==========================================
class Inventory:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.slots = ["Empty"] * capacity

    def add_item(self, item_name: str) -> bool:
        """Додає предмет у першу вільну комірку."""
        for i in range(self.capacity):
            if self.slots[i] == "Empty":
                self.slots[i] = item_name
                print(f"Додано '{item_name}' у слот {i}.")
                return True
        print(f"Інвентар повний! Неможливо додати '{item_name}'.")
        return False

    def remove_item(self, item_name: str) -> bool:
        """Видаляє предмет за назвою."""
        for i in range(self.capacity):
            if self.slots[i] == item_name:
                self.slots[i] = "Empty"
                print(f"Видалено '{item_name}' зі слота {i}.")
                return True
        print(f"Предмет '{item_name}' не знайдено.")
        return False

    def compact(self):
        """Ущільнює інвентар: предмет на початок, порожні в кінець."""
        non_empty = [item for item in self.slots if item != "Empty"]
        empty_count = self.capacity - len(non_empty)
        self.slots = non_empty + ["Empty"] * empty_count
        print("Інвентар ущільнено.")

    def display(self):
        print("Інвентар:", self.slots)


# ==========================================
# ДЕМОНСТРАЦІЯ РОБОТИ
# ==========================================
if __name__ == "__main__":
    print("--- ДЕМОНСТРАЦІЯ ОСНОВНИХ ЗАВДАНЬ ---")
    arr = generate_array(length=10, min_val=-10, max_val=10)
    print(f"Згенерований масив: {arr}")

    # 1
    cnt, total = count_and_sum_evens_in_range(arr, start_idx=2, end_idx=6)
    print(f"1. Парні з 2 по 6 індекс: кількість={cnt}, сума={total}")

    # 2
    avg, count_gt = avg_and_count_greater(arr)
    print(f"2. Середнє={avg:.2f}, більших за середнє={count_gt}")

    # 3 & 4
    arr2 = generate_array(length=10, min_val=1, max_val=5)
    print(f"3. Попарна сума з {arr2}: {pair_sum(arr, arr2)}")
    print(f"4. Конкатенація: {concatenate_arrays(arr, arr2)}")

    # 5
    print(f"5. Заміна max/min місцями: {swap_max_min(arr)}")

    # 6
    pos, neg = split_positive_negative(arr)
    print(f"6. Додатні: {pos}, Від'ємні: {neg}")

    # 7
    arr_dup = [1, 5, 1, 3, 5, 2]
    print(f"7. Видалення дублікатів max/min з {arr_dup}: {remove_max_min_duplicates(arr_dup)}")

    # 8
    print(f"8. Елементи між середніми: {filter_between_averages(arr, arr2)}")

    print("\n--- ДЕМОНСТРАЦІЯ ІГРОВОГО ІНВЕНТАРЮ ---")
    inv = Inventory(capacity=10)
    inv.add_item("Меч")
    inv.add_item("Зілля")
    inv.add_item("Щит")
    inv.display()

    inv.remove_item("Зілля")
    inv.display()

    inv.compact()
    inv.display()