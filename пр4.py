# 1. Від 1 до n
def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")


# 2. Від A до B
def print_a_to_b(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        print_a_to_b(a + 1, b)
    else:
        print_a_to_b(a - 1, b)


# 3. Точна степінь двійки
def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

def check_power_of_two(n):
    if is_power_of_two(n):
        print("YES")
    else:
        print("NO")


# 4. Сума цифр числа
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


# 5. Цифри числа справа наліво
def print_digits_reversed(n):
    if n == 0:
        return
    print(n % 10, end=" ")
    print_digits_reversed(n // 10)


# 6. Цифри числа зліва направо
def print_digits_direct(n):
    if n < 10:
        print(n, end=" ")
        return
    print_digits_direct(n // 10)
    print(n % 10, end=" ")


# --- Приклад виконання кожної задачі ---

if __name__ == "__main__":
    print("--- Задача 1 ---")
    n1 = int(input("Введіть n: "))
    print_1_to_n(n1)
    print("\n")

    print("--- Задача 2 ---")
    a = int(input("Введіть A: "))
    b = int(input("Введіть B: "))
    print_a_to_b(a, b)
    print("\n")

    print("--- Задача 3 ---")
    n3 = int(input("Введіть N: "))
    check_power_of_two(n3)
    print()

    print("--- Задача 4 ---")
    n4 = int(input("Введіть N: "))
    print("Сума цифр:", sum_digits(n4))
    print()

    print("--- Задача 5 ---")
    n5 = int(input("Введіть N: "))
    print_digits_reversed(n5)
    print("\n")

    print("--- Задача 6 ---")
    n6 = int(input("Введіть N: "))
    print_digits_direct(n6)
    print("\n")