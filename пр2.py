import random


# ==========================================
# ПОЧАТОК: Допоміжні функції для 2D-матриці
# ==========================================

def generate_matrix(m: int, n: int, min_val: int, max_val: int) -> list[list[int]]:
    """Генерує двовимірний масив (матрицю) m x n випадкових цілих чисел."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


def print_matrix(matrix: list[list]) -> None:
    """Виводить матрицю у форматованому вигляді з шапкою стовпців та рядків."""
    if not matrix or not matrix[0]:
        print("Матриця порожня.\n")
        return

    cols = len(matrix[0])

    # Шапка стовпців
    header = "\t\t" + "\t".join([f"стовпець {j + 1}" for j in range(cols)])
    print(header)

    # Виведення рядків (з округленням, якщо елементи float)
    for i, row in enumerate(matrix):
        row_str = "\t".join([f"{val:.2f}" if isinstance(val, float) else str(val) for val in row])
        print(f"рядок {i + 1}\t{row_str}")
    print()


# ==========================================
# ОСНОВНІ ЗАВДАННЯ (2D Матриці)
# ==========================================

def subtract_row_mean(matrix: list[list[int]]) -> list[list[float]]:
    """1. Віднімає від елементів кожного рядка його середнє арифметичне."""
    result = []
    for row in matrix:
        mean = sum(row) / len(row)
        result.append([round(val - mean, 2) for val in row])
    return result


def shift_matrix(matrix: list[list[int]], k: int) -> list[list[int]]:
    """2. Циклічний зсув матриці на k позицій вправо та на k догори."""
    m = len(matrix)
    n = len(matrix[0])
    shifted = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new_i = (i - k) % m  # Зсув догори
            new_j = (j + k) % n  # Зсув вправо
            shifted[new_i][new_j] = matrix[i][j]

    return shifted


def remove_max_rows_cols(matrix: list[list[int]]) -> list[list[int]]:
    """3. Знаходить максимальні елементи та видаляє всі рядки й стовпці, що їх містять."""
    m = len(matrix)
    n = len(matrix[0])

    # Пошук максимального значення
    max_val = max(max(row) for row in matrix)

    rows_to_remove = set()
    cols_to_remove = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == max_val:
                rows_to_remove.add(i)
                cols_to_remove.add(j)

    # Формування нової матриці
    new_matrix = []
    for i in range(m):
        if i in rows_to_remove:
            continue
        new_row = [matrix[i][j] for j in range(n) if j not in cols_to_remove]
        new_matrix.append(new_row)

    return new_matrix


def rotate_90_clockwise_inplace(matrix: list[list[int]]) -> None:
    """4. Поворот квадратної матриці на 90 градусів за годинниковою стрілкою (in-place)."""
    n = len(matrix)

    # Крок 1: Транспонування
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Крок 2: Реверс кожного рядка
    for i in range(n):
        matrix[i].reverse()


# ==========================================
# ДОДАТКОВЕ ЗАВДАННЯ (3D Розклад)
# ==========================================

EMPTY = "Вільне вікно"
DAYS = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]


def find_busiest_day(schedule: list, target_group: int) -> None:
    """Знаходить день із наибольшим навантаженням для обраної групи."""
    group_schedule = schedule[target_group]
    max_classes = -1
    busiest_day = ""

    for d_idx, day_schedule in enumerate(group_schedule):
        count = sum(1 for subject in day_schedule if subject != EMPTY)
        if count > max_classes:
            max_classes = count
            busiest_day = DAYS[d_idx]

    print(f"[Група {target_group + 1}] Найбільш завантажений день: {busiest_day} ({max_classes} пар(и)).")


def find_days_with_gaps(schedule: list, target_group: int) -> None:
    """Знаходить дні з вікнами між парами для обраної групи."""
    group_schedule = schedule[target_group]
    print(f"\n[Група {target_group + 1}] Перевірка днів на наявність «вікон»:")

    for d_idx, day_schedule in enumerate(group_schedule):
        class_indices = [p_idx for p_idx, subject in enumerate(day_schedule) if subject != EMPTY]

        if len(class_indices) >= 2:
            first_class = class_indices[0]
            last_class = class_indices[-1]

            has_gap = any(day_schedule[p] == EMPTY for p in range(first_class + 1, last_class))
            if has_gap:
                print(f"- {DAYS[d_idx]}: є вікна між парами.")


def check_stream_lectures(schedule: list) -> None:
    """Перевіряє наявність потокових занять."""
    print("\nПошук потокових занять:")
    found_any = False

    num_groups = len(schedule)
    num_days = len(schedule[0])
    num_pairs = len(schedule[0][0])

    for d in range(num_days):
        for p in range(num_pairs):
            for g1 in range(num_groups):
                subject1 = schedule[g1][d][p]
                if subject1 == EMPTY:
                    continue

                for g2 in range(g1 + 1, num_groups):
                    subject2 = schedule[g2][d][p]
                    if subject1 == subject2:
                        print(f"- {DAYS[d]}, Пара {p + 1}: '{subject1}' спільно у Групи {g1 + 1} та Групи {g2 + 1}")
                        found_any = True

    if not found_any:
        print("Потокових занять не знайдено.")


# ==========================================
# ГОЛОВНИЙ БЛОК ВИКОНАННЯ (MAIN)
# ==========================================

if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦІЯ ОСНОВНИХ ЗАВДАНЬ (2D МАТРИЦІ)")
    print("=" * 60)

    # Генеруємо початкову квадратну матрицю 4х4
    matrix = generate_matrix(4, 4, -5, 15)
    print("Початкова матриця 4x4:")
    print_matrix(matrix)

    # 1. Віднімання середнього арифметичного
    print("1. Матриця після віднімання середнього арифметичного рядка:")
    matrix_sub = subtract_row_mean(matrix)
    print_matrix(matrix_sub)

    # 2. Циклічний зсув (k = 1)
    k = 1
    print(f"2. Матриця після циклічного зсуву на {k} вправо та на {k} догори:")
    matrix_shifted = shift_matrix(matrix, k)
    print_matrix(matrix_shifted)

    # 3. Видалення рядків/стовпців з максимальними елементами
    print("3. Матриця після видалення рядків і стовпців з max елементом:")
    matrix_no_max = remove_max_rows_cols(matrix)
    print_matrix(matrix_no_max)

    # 4. Поворот на 90 градусів in-place
    print("4. Матриця після обертання на 90° за годинниковою стрілкою (in-place):")
    rotate_90_clockwise_inplace(matrix)
    print_matrix(matrix)

    print("=" * 60)
    print("ДЕМОНСТРАЦІЯ ДОДАТКОВОГО ЗАВДАННЯ (3D РОЗКЛАД)")
    print("=" * 60)

    # Створення масиву [3][5][4]
    schedule = [[[EMPTY for _ in range(4)] for _ in range(5)] for _ in range(3)]

    # Тестові дані
    # Група 1 (індекс 0), Пн: 3 пари
    schedule[0][0][0] = "Математика"
    schedule[0][0][1] = "Фізика"
    schedule[0][0][2] = "Програмування"

    # Група 1 (індекс 0), Вт: вікно на 2-й парі
    schedule[0][1][0] = "Історія"
    schedule[0][1][2] = "Англійська"

    # Потокова лекція у Ср, 1-ша пара для Групи 1 та Групи 2
    schedule[0][2][0] = "Вища Математика"
    schedule[1][2][0] = "Вища Математика"

    # Аналіз розкладу
    find_busiest_day(schedule, target_group=0)
    find_days_with_gaps(schedule, target_group=0)
    check_stream_lectures(schedule)