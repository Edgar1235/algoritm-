# ==========================================
# 1. РЕАЛІЗАЦІЯ ЧЕРГИ НА ОСНОВІ МАСИВУ
# ==========================================
class ArrayQueue:
    def __init__(self, capacity=13):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        """Додавання елемента в чергу."""
        if self.size == self.capacity:
            print("Помилка: Черга переповнена!")
            return False

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        print(f"[ArrayQueue] Додано елемент: {item}")
        return True

    def dequeue(self):
        """Видалення та повернення першого елемента з черги."""
        if self.is_empty():
            print("Помилка: Черга порожня!")
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        print(f"[ArrayQueue] Вилучено елемент: {item}")
        return item

    def get_size(self):
        """Повертає кількість елементів у черзі."""
        return self.size

    def is_empty(self):
        """Перевіряє, чи черга порожня."""
        return self.size == 0

    def display(self):
        """Виводить всі елементи черги у порядку FIFO."""
        if self.is_empty():
            print("[ArrayQueue] Черга порожня: []")
            return

        elements = []
        idx = self.head
        for _ in range(self.size):
            elements.append(str(self.queue[idx]))
            idx = (idx + 1) % self.capacity
        print(f"[ArrayQueue] Елементи черги (FIFO): -> [{', '.join(elements)}] ->")


# ==========================================
# 2. РЕАЛІЗАЦІЯ ЧЕРГИ НА ОСНОВІ ВУЗЛІВ (NODES)
# ==========================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Вказує на наступний вузол (address next node)


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        """Додавання елемента в чергу через вузол."""
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        print(f"[LinkedQueue] Додано елемент: {item}")

    def dequeue(self):
        """Видалення елемента з черги (початок Head переходить на next)."""
        if self.is_empty():
            print("Помилка: Черга порожня!")
            return None

        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1
        print(f"[LinkedQueue] Вилучено елемент: {item}")
        return item

    def get_size(self):
        """Повертає кількість елементів."""
        return self.size

    def is_empty(self):
        """Перевіряє, чи черга порожня."""
        return self.head is None

    def display(self):
        """Виводить вміст черги від Head до Tail."""
        if self.is_empty():
            print("[LinkedQueue] Черга порожня: []")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"[LinkedQueue] Елементи черги (FIFO): -> [{', '.join(elements)}] ->")


# ==========================================
# ДЕМОНСТРАЦІЯ РОБОТИ СТРУКТУР ДАНИХ
# ==========================================
if __name__ == "__main__":
    print("=== 1. ТЕСТУВАННЯ ЧЕРГИ НА МАСИВІ ===")
    arr_q = ArrayQueue(capacity=13)

    # Додавання елементів (за прикладом з Рис. 2 методички: 6, 4, 6, 2, 7)
    for val in [6, 4, 6, 2, 7]:
        arr_q.enqueue(val)

    arr_q.display()
    print(f"Кількість елементів: {arr_q.get_size()}")

    # Видалення елементів
    arr_q.dequeue()
    arr_q.dequeue()
    arr_q.display()
    print(f"Поточна кількість елементів: {arr_q.get_size()}\n")

    print("=== 2. ТЕСТУВАННЯ ЧЕРГИ НА ВУЗЛАХ (NODES) ===")
    link_q = LinkedQueue()

    # Додавання елементів (за прикладом з Рис. 3 методички: 12, 25, 8)
    for val in [12, 25, 8]:
        link_q.enqueue(val)

    link_q.display()
    print(f"Кількість елементів: {link_q.get_size()}")

    # Видалення елемента
    link_q.dequeue()
    link_q.display()
    print(f"Поточна кількість елементів: {link_q.get_size()}")