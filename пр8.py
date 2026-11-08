class Node:
    """Клас для представлення вузла бінарного дерева."""

    def __init__(self, value):
        self.value = value
        self.left = None  # Посилання на лівого нащадка (значення менше)
        self.right = None  # Посилання на правого нащадка (значення більше або рівне)


class BinarySearchTree:
    """Клас бінарного дерева пошуку."""

    def __init__(self):
        self.root = None
        self._count = 0

    def add(self, value):
        """Додавання елемента в дерево."""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self._count += 1
            print(f"[Додано корінь]: {value}")
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    self._count += 1
                    print(f"[Додано ліворуч]: {value} (до батьківського {current.value})")
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    self._count += 1
                    print(f"[Додано праворуч]: {value} (до батьківського {current.value})")
                    break
                current = current.right

    def contains(self, value):
        """Перевірка наявності елемента (пошук)."""
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        """Виведення та повернення найменшого елемента."""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        """Виведення та повернення найбільшого елемента."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def get_count(self):
        """Повертає кількість елементів у дереві."""
        return self._count

    def display_in_order(self):
        """Виведення всіх елементів у відсортованому порядку (In-order traversal)."""
        elements = []
        self._in_order_recursive(self.root, elements)
        print("Елементи дерева (In-order):", elements)

    def _in_order_recursive(self, node, elements):
        if node is not None:
            self._in_order_recursive(node.left, elements)
            elements.append(node.value)
            self._in_order_recursive(node.right, elements)

    def delete(self, value):
        """Видалення елемента з дерева."""
        if not self.contains(value):
            print(f"Помилка: Елемент {value} відсутній у дереві.")
            return False

        self.root = self._delete_recursive(self.root, value)
        self._count -= 1
        print(f"[Видалено елемент]: {value}")
        return True

    def _delete_recursive(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Випадок 1: Вузол без дітей або має лише одного нащадка
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Випадок 2: Вузол має обох нащадків
            # Шукаємо найменший елемент у правому піддереві (найбільш лівий вузол справа)
            min_node = self._get_min_node(current.right)
            current.value = min_node.value
            current.right = self._delete_recursive(current.right, min_node.value)

        return current

    def _get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


# ==========================================
# ДЕМОНСТРАЦІЯ РОБОТИ СТРУКТУРИ ДАНИХ
# ==========================================
if __name__ == "__main__":
    bst = BinarySearchTree()

    print("=== 1. ДОДАВАННЯ ЕЛЕМЕНТІВ ===")
    # Будуємо дерево відповідно до прикладу з методички
    elements_to_add = [3, 1, 9, 1, 7, 10, 6, 8]
    for val in elements_to_add:
        bst.add(val)

    print("\n=== 2. ІНФОРМАЦІЯ ПРО ДЕРЕВО ===")
    bst.display_in_order()
    print(f"Загальна кількість елементів: {bst.get_count()}")
    print(f"Найменший елемент: {bst.find_min()}")
    print(f"Найбільший елемент: {bst.find_max()}")

    print("\n=== 3. ПОШУК ЕЛЕМЕНТІВ ===")
    print(f"Чи є елемент 7 у дереві? {bst.contains(7)}")
    print(f"Чи є елемент 15 у дереві? {bst.contains(15)}")

    print("\n=== 4. ВИДАЛЕННЯ ЕЛЕМЕНТІВ ===")
    # Видалення вузла з двома нащадками (3)
    bst.delete(3)
    bst.display_in_order()
    print(f"Поточна кількість елементів: {bst.get_count()}")
    print(f"Новий корінь (мінімум піддерева): найменший елемент {bst.find_min()}, найбільший {bst.find_max()}")